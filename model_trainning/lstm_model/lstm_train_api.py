# That train and save the model for tracked stock
from env import env
from pymongo import MongoClient
import pandas as pd
from flask import Blueprint, request
import json
import os 
from logger import logger
from datetime import datetime
import numpy as np

lstm_model_train_module = Blueprint(env.route_lstm_training_model, __name__)

client = MongoClient(env.URL_MONGO, 27017)
db = client[env.DB_NAME]
collection_stocks_data = db[env.COLLECTION_NAME_SP500_STOCKS_DATA]
collection_lstm_training_data = db[env.COLLECTION_LSTM_TRAINING_DATA]

@lstm_model_train_module.route(env.route_lstm_training_model,methods=['POST'])
def train_lstm_model() -> dict:
    data: dict = request.get_json()
    print("LSTM Trainer:", data)
    stock_title: str = data['stock_title']

    lstm_model_path: str = env.lstm_model_path + f"{stock_title}_lstm.h5"
    lstm_scaler_path:str = env.lstm_model_path + f"{stock_title}_lstm_scaler.save"

    # check if model if already exits and saved 
    if os.path.exists(lstm_model_path) and os.path.exists(lstm_scaler_path):
        logger.info(f"LSTM MODEL TRAINNER:LSTM model already exist for {stock_title}, will skip training")
        print("Model already exists")
        return {"status": " lstml model already exists"}, 200

    # start training new model
    logger.info(f"LSTM MODEL TRAINNER:LSTM model not found {stock_title}, starting training")
    stock_data: dict = collection_stocks_data.find_one({"stock_title": stock_title})
    if not stock_data:
        return {"status": "stock not found"}, 404
    df_str: str = stock_data['data_frame']
    if not df_str:
        return {"status": "no data for stock"}, 400
    df: pd.DataFrame = pd.DataFrame(json.loads(df_str))

    # data preparation 
    from sklearn.preprocessing import MinMaxScaler

    # Sort by date
    df = df.sort_values('Date')

    # Scale only the 'Close' column for prediction
    scaler = MinMaxScaler()
    df['Close_scaled'] = scaler.fit_transform(df[['Close']])

    sequence_length = env.lstm_sequence_length  # e.g., use past 60 days to predict next 5
    future_days = env.lstm_future_days

    # Split data features and y
    X, y = [], []
    print(type(X))
    for i in range(len(df) - sequence_length - future_days + 1):
        X.append(df['Close_scaled'].values[i:i+sequence_length])
        y.append(df['Close_scaled'].values[i+sequence_length:i+sequence_length+future_days])

    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))  # LSTM expects 3D input
    
    # Models create
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
    import joblib

    model = Sequential([
    LSTM(64, return_sequences=False, input_shape=(X.shape[1], 1)),
    Dense(future_days)
    ])

    model.compile(optimizer='adam', loss='mse')
    model.summary()

    # chekpoint and save best model 
    checkpoint = ModelCheckpoint(
    lstm_model_path,       # file to save
    monitor='val_loss',         # what to monitor
    save_best_only=True,        # only save if val_loss improves
    mode='min',                 # lower val_loss is better
    verbose=1)   

    # when to stop and which model to save 
    early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,            # wait 10 epochs for improvement
    restore_best_weights=True)

    #model fit
    history = model.fit(
    X, y,
    epochs=1000,
    batch_size=32,
    validation_split=0.1,
    callbacks=[checkpoint, early_stop])

    # Save scaler
    joblib.dump(scaler, lstm_scaler_path)

    # pull metrics and store to mongo db 
    # After training
    final_train_mse = history.history['loss'][-1]
    final_val_mse = history.history['val_loss'][-1]

    collection_lstm_training_data.insert_one({"training_date": datetime.now(),
                                              "stock_title": stock_title, 
                                              "loss_mse": final_train_mse,
                                              "val_loss": final_val_mse})
        
    logger.info(f"MODEL TRAINNER:Model trained for {stock_title} finished and saved, with MAR: {final_val_mse}")


    return {"status":"succes"}
