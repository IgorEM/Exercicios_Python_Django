import json
import settings
import requests

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
# **kwargs - numero ilimitado de argumentos. adjusted="false",outputsize="compact"
class APICallError(Exception):
    pass

class IntervalInvalid(Exception):
    pass

class StockTimeSeries:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY


    def _build_url(self,path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    def TratandoKwargs(self, kwargs, path):
        lista = []
        for c, v in kwargs.items():
            lista.append(f"{c}={v}")
        if lista:
            path = f"{path}&{'&'.join(lista)}"
        else:
            path


    def intraday_series(self,function,symbol,interval, **kwargs):
        #function = TIME_SERIES_INTRADAY & symbol = IBM & interval = 5min
        if interval in ("1min", "5min", "15min", "30min", "60min"):
            path = f"function={function}&symbol={symbol}&interval={interval}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("Intervalo Inválido")
            raise IntervalInvalid("Intervalo invalido. Os intervalos válidos são: 1min,5min,15min,30min,60min")


        url = self._build_url(path)

        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()
        raise APICallError(f"Não foi possivel consumir o serviço: {url}")

obj_sts = StockTimeSeries()
dados = obj_sts.intraday_series("TIME_SERIES_INTRADAY", "IBM", "60min", adjusted="false", outputsize="compact")
print(dados)



