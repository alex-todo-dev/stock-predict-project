# That module will pick up close price and predict the future price for the next day 
from flask import Flask, request, Blueprint
from env import env
from logger import logger
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['stock_predict']
collection = db['buy_signal_track']

prediction_module_lstm = Blueprint(env.route_start_lstm_prediction, __name__)
# Pull all tracked stock from buy_signal_track collection

client = MongoClient('localhost', 27017)
db = client['stock_predict']
collection_stock_data = db['sp500_stocks_data']
collection_stocks_under_tracking = db['buy_signal_track']

@prediction_module_lstm.route(env.route_start_lstm_prediction, methods=['GET'])
def predict_price():
    pass 