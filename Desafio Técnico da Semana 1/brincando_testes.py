import json
import settings
import requests
from main import StockTimeSeries

# testando requests
url= ("https://www.alphavantage.co/query?"
      "function=TIME_SERIES_INTRADAY"
      "&symbol=IBM"
      "&interval=5min&apikey=demo")

r = requests.get(url)
print(f"r : {r}")

data = r.json()
print(f"data :{data}")

with open("data.json","w") as fp:
     fp.write(json.dumps(data, indent=4))

#testando class
obj_sts = StockTimeSeries()
path = obj_sts.intraday_series("TIME_SERIES_INTRADAY","IBM","5min")
print(path)
print(obj_sts._build_url(path))

#testando problema do **kwargs
d = {'a': 1, 'b': 2}
l = [f"{k[0]}={k[1]}" for k in d.items()]

lista = []

for c, v in d.items():
    lista.append(f"{c}={v}")

print(lista)