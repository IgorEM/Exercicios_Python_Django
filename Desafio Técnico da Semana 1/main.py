import json
import settings
import requests

#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
# **kwargs - numero ilimitado de argumentos. vamos simular um dicionario
class APICallError(Exception):
    pass


class StockTimeSeries:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY


    def _build_url(self,path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"


    def intraday_series(self,function,symbol,interval, **kwargs):
        #function = TIME_SERIES_INTRADAY & symbol = IBM & interval = 5min
        #lista = []
        if interval == '1min' or '5min' or '15min' or '30min' or '60min':
            path = f"function={function}&symbol={symbol}&interval={interval}"
            options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
            path = f"{path}&{'&'.join(options)}" if options else path
            # for c, v in kwargs.items():
            #     lista.append(f"{c}={v}")
            # if lista:
            #     path = f"{path}&{'&'.join(lista)}"
            # else:
            #     path
        else:
            print("Intervalo Inválido")

        url = self._build_url(path)

        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()
        raise APICallError(f"Não foi possivel consumir o serviço: {url}")

        #return path





obj_sts = StockTimeSeries()
dados = obj_sts.intraday_series("TIME_SERIES_INTRADAY","IBM","5min")
print(dados)



