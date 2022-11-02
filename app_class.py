from tkinter import *
from tkinter import ttk
from datetime import datetime
from config import IMAGE
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
            font=("franklin gothic medium", 10)
            )

        self.date.place(x=200, y=15, anchor="center")

        # 'From' & 'To' Labels
        self.from_currency = Label(
            self,
            text="From",
            bg="#808b96",
            fg="white",
            font=("franklin gothic medium", 10)
            )

        self.from_currency.place(x=100, y=50, anchor="center")

        self.to_currency = Label(
            self,
            text="To",
            bg="#808b96",
            fg="white",
            font=("franklin gothic medium", 10)
        )

        self.to_currency.place(x=300, y=50, anchor="center")

        # 'From' & 'To' Entry Boxes
        self.from_currencies = StringVar(self)
        self.from_currencies.set("USD")

        self.from_box = ttk.Combobox(
            self,
            width=20,
            textvariable=self.from_currencies,
            values=list(self.__get_currencies()),
            state="readonly"
        )

        self.from_box.place(x=100, y=75, anchor="center")

        self.to_currencies = StringVar(self)
        self.to_currencies.set("EUR")

        self.to_box = ttk.Combobox(
            self,
            width=20,
            textvariable=self.to_currencies,
            values=list(self.__get_currencies()),
            state="readonly"
        )

        self.to_box.place(x=300, y=75, anchor="center")

        # 'Amount' Label & Entry Box
        self.amount = Label(
            self,
            text="Amount",
            bg="#808b96",
            fg="white",
            font=("franklin gothic medium", 10)
        )

        self.amount.place(x=200, y=125, anchor="center")

        self.amount_box = Entry(self)

        self.amount_box.place(x=200, y=150, anchor="center", width=200)

        # 'Output' Label
        self.output = Label(
            self,
            text="",
            bg="white",
            fg="black",
            font=("franklin gothic medium", 10),
            relief="sunken",
            width=15
        )

        self.output.place(x=200, y=200, anchor="center")

        # 'Convert' Button
        self.convert = Button(
            self,
            text="Convert",
            bg="#27ae60",
            fg="white",
            font=("franklin gothic medium", 10),
            width=10,
            command=self.__convert_amount
        )

        self.convert.place(x=100, y=275, anchor="center")

        # 'Clear' Button
        self.clear = Button(
            self,
            text="Clear",
            bg="#27ae60",
            fg="white",
            font=("franklin gothic medium", 10),
            width=10,
            command=self.__clear_queries
        )

        self.clear.place(x=200, y=275, anchor="center")

        # 'Exit' Button
        self.exit = Button(
            self,
            text="Exit",
            bg="#27ae60",
            fg="white",
            font=("franklin gothic medium", 10),
            width=10,
            command=self.destroy
        )

        self.exit.place(x=300, y=275, anchor="center")

    def __connect_to_api(self):
        """
        Connects to the API that provides the rates and conversion.
        """
        
        url = f"https://api.exchangerate.host/convert?from={self.from_currencies.get()}&to={self.to_currencies.get()}&amount={self.amount_box.get()}"

        response = requests.get(url)
        data = response.json()

        return data

    def __get_currencies(self):
        """
        Returns the currencies supported by the API.
        """

        url = "https://api.exchangerate.host/latest"

        response = requests.get(url)
        data = response.json()

        rates = data.get("rates")

        return rates

    def __convert_amount(self):
        """
        Returns the amount of the exchange.
        """
        result = self.__connect_to_api()["result"]

        return self.output.config(text=f"{result}")

    def __clear_queries(self):
        input_box = self.amount_box.delete(0, END)
        output_box = self.output.config(text="")

        return input_box, output_box