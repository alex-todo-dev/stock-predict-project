from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Connect to your local MongoDB or Atlas
client = MongoClient("mongodb://localhost:27017/")  # or your Mongo URI
db = client["stock_predict"]  # your database name
tracked_stocks_collection = db["buy_signal_track"]  # your collection name
trade_stock_data_collection = db["sp500_stocks_data"]
training_data_collection = db["training_data"]
prediction_metrics_collection = db["tracked_stock_metrics"]

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Stock Predictor Home Page api!"

@app.route("/stock-data/<stock>", methods=["GET"])
def stock_data(stock: str) -> dict:
    stock_data = trade_stock_data_collection.find_one({"stock_title": stock},{'_id': 0})
    return jsonify(stock_data) 

@app.route("/tracked-stocks/<stock>")
def tracked_stocks(stock: str):
    tracked_stocks = tracked_stocks_collection.find({"stock_title": stock},{'_id': 0})
    return jsonify(tracked_stocks)

@app.route("/buy-signal-all-stocks")
def all_tracked_stocks():
    all_tracked_stocks = tracked_stocks_collection.find({},{'_id': 0})
    return jsonify(list(all_tracked_stocks))

@app.route("/training-data/<stock>")
def training_data(stock: str):
    stock_training_data = training_data_collection.find_one({"stock_title": stock},{'_id': 0})
    return jsonify(stock_training_data)

@app.route("/result-data/<stock>")
def result_data(stock: str):
    prediction_result_data = prediction_metrics_collection.find_one({"stock_title": stock},{'_id': 0})
    return jsonify(prediction_result_data)

if __name__ == "__main__":
    app.run(port=5001, debug=True)
