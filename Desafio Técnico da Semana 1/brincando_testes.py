import requests
import json

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

