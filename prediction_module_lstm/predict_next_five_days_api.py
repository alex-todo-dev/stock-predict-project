# That module will pick up close price and predict the future price for the next day 
from flask import Flask, request, Blueprint
from env import env
from logger import logger
from pymongo import MongoClient
from datetime import datetime

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

prediction_module_lstm = Blueprint(env.route_start_lstm_prediction, __name__)
# Pull all tracked stock from buy_signal_track collection

client = MongoClient('localhost', 27017)
db = client['stock_predict']
collection_stock_data = db['sp500_stocks_data']
collection_stocks_under_tracking = db['buy_signal_track']
collection_lstm_prediction = db['lstm_prediction']
@prediction_module_lstm.route(env.route_start_lstm_prediction, methods=['GET'])
def predict_price():
    print("Staring lsmt prediction")
    tracked_stocks = collection_stocks_under_tracking.find()
    tracked_stocks_list = list(tracked_stocks)
    for tracked_stock in tracked_stocks_list:
        tracked_stock_title = tracked_stock.get('stock_title')
        first_buy_signal_date = tracked_stock.get('first_buy_signal_data')
        tracking_data_14_days = tracked_stock.get('days_tracking')

        # Check if lstm if already predicted for next five work days 
        

        # Loadind model and scaler 
        from tensorflow.keras.models import load_model
        import joblib
        try:
            model = load_model(env.lstm_model_path  + tracked_stock_title + '_lstm.h5' , compile=False)
            scaler = joblib.load(env.lstm_model_path + tracked_stock_title + '_lstm_scaler.save')
        except:
            print('Failed to load the model')

        print(f'Loaded data for lstm model {tracked_stock_title}')

    return {"status":"lstm prediction finished"}