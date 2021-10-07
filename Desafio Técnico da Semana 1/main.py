import json
import settings
import requests
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
# **kwargs - numero ilimitado de argumentos. adjusted="false",outputsize="compact"
class APICallError(Exception):
    pass

class IntervalInvalid(Exception):
    pass

class FunctionInvalid(Exception):
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

    def BuildTestRequisicao(self, path):
        url = self._build_url(path)
        resp = requests.get(url)
        if resp.status_code == 200:
            return print(resp.json())
        raise APICallError(
            f"Não foi possível consumir o serviço: "
            f"\n STATUS_CODE: \n "
            f"{resp.status_code}"
        )

    def intraday_series(self,function,symbol,interval, **kwargs):
        #function = TIME_SERIES_INTRADAY & symbol = IBM & interval = 5min
        if interval in ("1min", "5min", "15min", "30min", "60min"):
            path = f"function={function}&symbol={symbol}&interval={interval}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("Intervalo Inválido")
            raise IntervalInvalid("Intervalo invalido. Os intervalos válidos são: 1min,5min,15min,30min,60min")

        self.BuildTestRequisicao(path)


    def intraday_series_extendHistory(self,function,symbol,interval,slice,**kwargs):
        #function = TIME_SERIES_INTRADAY_EXTENDED & symbol = IBM & interval = 15min & slice = year1month1
        if interval in ("1min", "5min", "15min", "30min", "60min"):
            path = f"function={function}&symbol={symbol}&interval={interval}&slice={slice}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("Intervalo Inválido")
            raise IntervalInvalid("Intervalo invalido. Os intervalos válidos são: 1min,5min,15min,30min,60min")

        self.BuildTestRequisicao(path)

    def dayly(self,function,symbol,**kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_DAILY":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_DAILY")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def dayly_adjusted(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_DAILY_ADJUSTED":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_DAILY_ADJUSTED")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def weekly(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_WEEKLY":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_WEEKLY")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def weekly_adjusted(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_WEEKLY_ADJUSTED":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_WEEKLY_ADJUSTED")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def monthly(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_MONTHLY":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_MONTHLY")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def monthly_adjusted(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "TIME_SERIES_MONTHLY_ADJUSTED":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=TIME_SERIES_MONTHLY_ADJUSTED")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def quote_endpoint(self, function, symbol, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "GLOBAL_QUOTE":
            path = f"function={function}&symbol={symbol}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=GLOBAL_QUOTE")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

    def search_endpoint(self, function, keywords, **kwargs):
        # function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
        if function == "SYMBOL_SEARCH":
            path = f"function={function}&keywords={keywords}"
            self.TratandoKwargs(kwargs, path)
        else:
            print("função inválida.Função tem que ser function=SYMBOL_SEARCH")
            raise FunctionInvalid("função inválida.")

        self.BuildTestRequisicao(path)

obj_sts = StockTimeSeries()

print("\nIntraday_series:")
dados = obj_sts.intraday_series("TIME_SERIES_INTRADAY", "IBM", "60min", adjusted="false", outputsize="compact")

print("\nIntraday_series_extedHistory:")
dados1 = obj_sts.intraday_series_extendHistory("TIME_SERIES_INTRADAY", "IBM", "60min","year1month3", adjusted="true")

print("\nDayly:")
dados2 = obj_sts.dayly("TIME_SERIES_DAILY", "TSCO.LON",outputsize="full")

print("\nDayly_adjusted:")
dados3 = obj_sts.dayly_adjusted("TIME_SERIES_DAILY_ADJUSTED", "RELIANCE.BSE",outputsize="full")

print("\nWeekly:")
dados4 = obj_sts.weekly("TIME_SERIES_WEEKLY", "IBM")

print("\nWeekly Adjusted:")
dados5 = obj_sts.weekly_adjusted("TIME_SERIES_WEEKLY_ADJUSTED", "TSCO.LON")

print("\nMontly:")
dados6 = obj_sts.monthly("TIME_SERIES_MONTHLY", "IBM")

print("\nMontly Adjusted:")
dados7 = obj_sts.monthly_adjusted("TIME_SERIES_MONTHLY_ADJUSTED", "IBM")

print("\nQuote Endpoint:")
dados8 = obj_sts.quote_endpoint("GLOBAL_QUOTE", "IBM")

print("\nSearch Endpoint:")
dados9 = obj_sts.search_endpoint("SYMBOL_SEARCH", "tesco")




