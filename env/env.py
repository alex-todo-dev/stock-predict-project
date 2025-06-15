# flask routes
# base route 
base_url = 'http://127.0.0.1:5000'
#  store data to mongo
route_store_data_mongo = '/trend-calculation-store-to-db'
#  indicator calculation
route_indicator_calculation = '/indicators_generation'
#  collect buy signal
route_collect_buy_signal = '/collect-buy-signal-stock'
# nn_training_model 
route_nn_training_model = '/nn-training-model'
# cleaner module
route_cleaner_module = '/cleaner-module'
# price predictor route 
route_price_predictor = '/predict-price'
# data pull route
route_stock_data_pull = '/stock-data-pull'
# model prepare route
route_model_train = '/model-train'
# model prediction route
route_prediction_module = '/prediction'
# start stocks prediction route 
route_start_prediction = '/prediction'
# tracked stock metrics calculation route
route_tracked_stocks_metrics = '/tracked-stocks-metrics'
# news anylysis route
route_news_analysis = '/news-analysis'
# packages NAMES 
# first_stock_data_fetch
first_data_fetch_module_name = 'FIRST_DATA_FETCH_MODULE'
# stock_indicator_calculation
stock_indicator_calculation_module_name = 'STOCK_INDICATOR_CALCULATION_MODULE'
# store_data_to_monog
store_data_mongo_name = 'STORE_DATA_TO_MONGO_MODULE'
# collect_buy_signal_stock
collect_buy_signal_name = 'COLLECT_BUY_SIGNAL_MODULE'
# cleaner module 
cleaner_module_name = 'CLEANER_MODULE'
# stock names
STOCK_CSV_DATA_FAIL = "constituents.csv"
# Mongo database setup
# db url
URL_MONGO = "mongodb://localhost:27017/"
# db name
DB_NAME = "stock_predict"
# collection names
COLLECTION_NAME_STOCKS_UNDER_TRACKING = "buy_signal_track"
# SP 500 stock data pull days
COLLECTION_NAME_SP500_STOCKS_DATA = "sp500_stocks_data"
# colection training data 
COLLECTION_NAME_TRAINING_DATA = "training_data"
# Mongo DB port number 
MONGO_DB_PORT_NUMBER = 27017
# stock filled name 
STOCK_TITLE_FILED_NAME = "stock_title"
# 14 days tracking filled 
TRACKING_FIELD_NAME_14_DAYS = "days_tracking"
# path for NN models store 
model_path: str = f"model_trainning/nn_model/models/"
# days pull for stock data
stock_data_pull_days = 365
# stock cleaner days old 
cleaner_days_old = 14
# RSI treshold 
RSI_THRESHOLD = 30
# BUY SIGAL COEFFICIENT
BUY_SIGNAL_COEFFICIENT = 1
# Moving average window size 
MOVING_AVERAGE_WINDOW_SIZE = 14
# RSI window size
RSI_WINDOW_SIZE = 14
# Column for calculations  - close 
COLUMN_CALCULATION_NAME_RSI = 'Close'
# Stock title
STOCK_TITLE_FILED_NAME = 'stock_title'
# NUMBER OF STOCKS TO RUN 
NUMBER_OF_STOCKS_TO_RUN = 450
# FININ KEY 
FIN_KEY = "*********"
