import requests
import json

class Converter():
    def __init__(self, from_currency:str, to_currency:str, amount:int):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.__places = 2
        self.__host = None

    def __connect_to_api(self):
        """
        Connects to an API that provides the rates and conversion.
        """

        url = f"https://api.exchangerate.host/convert?from={self.from_currency}&to={self.to_currency}&amount={self.amount}&places={self.__places}"

        response = requests.get(url)
        data = response.json()

        return data

    def get_currencies(self):
        """
        Returns the currencies supported by the API.
        """

        url = "https://api.exchangerate.host/latest"

        response = requests.get(url)
        data = response.json()

        rates = data.get("rates")

        return rates

    def convert_amount(self):
        """
        Returns the amount returned after the currency exchange was made.
        """

        return self.__connect_to_api()["result"]

    def exchange_rate(self):
        """
        Returns the rate at which the exchange was made.
        """

        return self.__connect_to_api()["info"]["rate"]
