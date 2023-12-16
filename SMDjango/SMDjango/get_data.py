import time
import json
import requests
import pandas as pd
from dateutil.parser import parse

'''
Get Data When Requests
instrument
start
ended
'''

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

def get_share_price(instrument, start, ended):
    StockExchange = instrument.split(".")[1]
    date_range = pd.date_range(start=start, end=ended, freq='D')
    share_price = pd.DataFrame()
    Result = []
    if StockExchange == "SS":
        instrument = instrument.split(".")[0]
        for date in date_range:
            timeArray = time.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            timestamp = int(time.mktime(timeArray))
            formatted_date = time.strftime("%Y%m%d", timeArray)
            jquery = f'jQuery11240884023465957779_{timestamp}'
            api = f'https://yunhq.sse.com.cn:32042/v1/sh1/mink/{instrument}?callback={jquery}&select=date%2Cclose%2CprevClose%2Cvolume%2Chigh%2Clow%2Cavg&begin=0&end=-1&period={formatted_date}&_={timestamp}'
            res = requests.get(api, headers=header)
            result = json.loads(res.text[len(jquery) + 1:-1])
            items = result['kline']
            for data in items:
                # Date = parse(str(data[0])).strftime("%Y-%m-%d %H:%M:%S")
                Date = data[0]
                Price = data[1]
                Result.append([Date, Price])
                columns = {
                    "Date": [parse(str(data[0])).strftime("%Y-%m-%d %H:%M:%S")],
                    "Open": data[2],
                    "High": data[4],
                    "Low": data[5],
                    "Close": data[1],
                    "Average": data[6],
                    "Volume": data[3],
                }
                share_price = pd.concat([share_price, pd.DataFrame(columns)], axis=0)

    if StockExchange == "SZ":
        instrument = instrument.split(".")[0]
        api = f"https://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.2024269370830547&marketId=1&code={instrument}"
        res = requests.get(api, headers=header)
        result = json.loads(res.text)
        items = result['data']['picupdata']

        for data in items:
            columns = {
                "Date": [f"{data[0]}"],
                "Open": [float(data[1])],
                "High": [float(data[1])],
                "Low": [float(data[5])],
                "Close": [float(data[1])],
                "Average": [float(data[2])],
                "Volume": [float(data[6])],
            }
            share_price = pd.concat([share_price, pd.DataFrame(columns)], axis=0)

    # return share_price.to_json(orient='records')
    return Result

if __name__ == "__main__":
    instrument = "002230.SZ"
    start = "2023-11-21 15:30:00"
    ended = "2023-12-01 15:30:00"
    share_price = get_share_price(instrument, start, ended)
    print(share_price)


