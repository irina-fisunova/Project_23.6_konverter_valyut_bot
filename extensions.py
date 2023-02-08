import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
       if quote == base:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты {base}.")

       try:
            quote_ticker = keys[quote]
       except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

       try:
            base_ticker = keys[base]
       except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

       try:
            amount = float(amount)
       except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}.")

       r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
       single_cost = float(json.loads(r.content)[keys[base]])
       total_cost = single_cost * float(amount)

       cost = {
           'single': str(round(single_cost, 2)),
           'total': str(round(total_cost, 2))
       }


       return cost