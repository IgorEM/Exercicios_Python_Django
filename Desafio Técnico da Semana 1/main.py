import json
import settings
import requests

class StockTimeSeries:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY


    def _build_url(self,path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"


    def Intraday(self,symbol,interval):
        if interval == '1min' or '5min' or '15min' or '30min' or '60min':
            path = "function="
            #https: // www.alphavantage.co / query?function = TIME_SERIES_INTRADAY & symbol = IBM & interval = 5min & apikey = demo
# sts = StockTimeSeries()
# print(sts)
