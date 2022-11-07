from tkinter import *
from tkinter import ttk
from datetime import datetime
from config import *
import tkinter as tk
import requests

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main Window
        self.title("Currency Converter")
        self.geometry("400x400")
        self.config(bg="#808b96")
        self.resizable(False, False)
        self.iconbitmap(IMAGE)

        # 'Date' Label
        self.date = Label(
            self, 
            text=datetime.now().strftime("%d %B %Y"), 
            bg="#808b96", 
            fg="white", 
            font=(FONT_TYPE, FONT_SIZE)
            )

        self.date.place(x=200, y=15, anchor="center")

        # 'From' & 'To' Labels
        self.from_currency = Label(
            self,
            text="From",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE)
            )

        self.from_currency.place(x=100, y=50, anchor="center")

        self.to_currency = Label(
            self,
            text="To",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE),
        )

        self.to_currency.place(x=300, y=50, anchor="center")

        # 'From' & 'To' Entry Boxes
        self.from_currencies = StringVar(self)
        self.from_currencies.set("USD - United States Dollar")

        self.from_box = ttk.Combobox(
            self,
            width=25,
            textvariable=self.from_currencies,
            values=list(self.__get_currencies()),
            state="readonly",
            justify="center"
        )

        self.from_box.place(x=100, y=75, anchor="center")

        self.to_currencies = StringVar(self)
        self.to_currencies.set("EUR - Euro")

        self.to_box = ttk.Combobox(
            self,
            width=25,
            textvariable=self.to_currencies,
            values=list(self.__get_currencies()),
            state="readonly",
            justify="center"
        )

        self.to_box.place(x=300, y=75, anchor="center")

        # 'Amount' Label & Entry Box
        self.amount = Label(
            self,
            text="Amount",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE)
        )

        self.amount.place(x=200, y=125, anchor="center")

        self.amount_box = Entry(
            self, 
            justify="center"
            )

        self.amount_box.place(x=200, y=150, anchor="center", width=200)

        # 'Rate' Label
        self.rate = Label(
            self,
            text="Conversion Rate",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE)
        )

        self.rate.place(x=200, y=185, anchor="center")

        self.rate_output = Label(
            self,
            text="",
            bg="white",
            fg="black",
            font=(FONT_TYPE, FONT_SIZE),
            relief="sunken",
            width=20,
            justify="center"
        )

        self. rate_output.place(x=200, y=210, anchor="center")

        # 'Conversion' Label
        self.conversion = Label(
            self,
            text="Output",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE)
        )

        self.conversion.place(x=200, y=245, anchor="center")

        self.conversion_output = Label(
            self,
            text="",
            bg="white",
            fg="black",
            font=(FONT_TYPE, FONT_SIZE),
            relief="sunken",
            width=20,
            justify="center"
        )

        self.conversion_output.place(x=200, y=270, anchor="center")

        # 'Convert' Button
        self.convert = Button(
            self,
            text="Convert",
            bg="#27ae60",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE),
            width=10,
            command=self.__convert_amount
        )

        self.convert.place(x=100, y=325, anchor="center")

        # 'Clear' Button
        self.clear = Button(
            self,
            text="Clear",
            bg="#27ae60",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE),
            width=10,
            command=self.__clear_queries
        )

        self.clear.place(x=200, y=325, anchor="center")

        # 'Exit' Button
        self.exit = Button(
            self,
            text="Exit",
            bg="#27ae60",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE),
            width=10,
            command=self.destroy
        )

        self.exit.place(x=300, y=325, anchor="center")

        # 'Version' Label
        self.version = Label(
            self,
            text="v1.2",
            bg="#808b96",
            fg="white",
            font=(FONT_TYPE, FONT_SIZE)
        )

        self.version.place(x=385, y=390, anchor="center")

    def __connect_to_api(self):
        """
        Connects to the API that provides the rates and conversion.
        """
        try:
            url = f"https://api.exchangerate.host/convert?from={self.from_currencies.get()[0:3]}&to={self.to_currencies.get()[0:3]}&amount={self.amount_box.get()}&source={DATA_SOURCE}"
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)

        response = requests.get(url)
        data = response.json()

        return data

    def __get_currencies(self):
        """
        Returns the currencies supported by the API.
        """
        try:
            url = "https://api.exchangerate.host/symbols"
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)

        response = requests.get(url)
        data = response.json()

        symbols = data["symbols"]

        for code, name in symbols.items():
            yield code + " - " + name["description"]

    def __convert_amount(self):
        """
        Returns the amount and the rate at which the exchange was made.
        """
        result = self.__connect_to_api()["result"]
        rate = self.__connect_to_api()["info"]["rate"]

        return self.conversion_output.config(text=f"{result:.2f}"), self.rate_output.config(text=f"1 {self.from_currencies.get()[0:3]} = {rate} {self.to_currencies.get()[0:3]}")

    def __clear_queries(self):
        """
        Clears the queries in the GUI.
        """
        input_box = self.amount_box.delete(0, END)
        output_box = self.conversion_output.config(text="")
        rate_box = self.rate_output.config(text="")

        return input_box, output_box, rate_box
