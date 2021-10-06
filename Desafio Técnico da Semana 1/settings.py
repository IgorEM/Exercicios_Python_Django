from decouple import config

APIKEY = config("APIKEY")
BASE_URL = config("BASE_URL", "https://www.alphavantage.co/query")
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
