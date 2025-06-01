from pymongo import MongoClient
import pandas as pd
import json
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client['stock_predict']
collection_buy_signal = db['buy_signal_track']
collection_stock_data = db['sp500_stocks_data']


buy_signal_date = datetime(2025, 4, 9)

stock_title = "ALGN"

# Pulling data from stock data and stock tracking collection 
stock_data = collection_stock_data.find_one({"stock_title": stock_title})
track_data_doc = collection_buy_signal.find_one({"stock_title": stock_title})

# Loading data table with last year data
stock_data_df = pd.DataFrame(json.loads(stock_data['data_frame']))
stock_data_df['Date'] = pd.to_datetime(stock_data_df['Date'])

dates_after_buy_signal_date = stock_data_df[stock_data_df['Date'] >= buy_signal_date]

# Loading tracked dates 
track_data_dates = track_data_doc['14_days_tracking']
tracked_dates = [date.get['date'] for date in track_data_dates]


print("Trakced days:", tracked_dates)
print("Stock data:", dates_after_buy_signal_date)
# filter rows where not tracked dates 

missed_tracked_dates = dates_after_buy_signal_date[~dates_after_buy_signal_date['Date'].isin(tracked_dates)]
for index, row in missed_tracked_dates.iterrows():
    last_date_day_pull_datetime = row['Date']
    closing_price = row['Close']
    new_stock_value = {"date": last_date_day_pull_datetime, "closing_price": closing_price, "predicted_price": False}
    print(f"Adding {new_stock_value} to {stock_title} in buy signal track")
    track_data_dates.append(new_stock_value)
    track_data_dates.sort(key=lambda x: x['date'])
    print("New tracked list", track_data_dates)
    update_result = collection_buy_signal.update_one({"_id": track_data_doc['_id']}, {"$set": {"14_days_tracking": track_data_dates}})
    print("Updated result:", update_result.modified_count)
print("missed dates:", missed_tracked_dates)

