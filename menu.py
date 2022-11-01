from tkinter import *
from tkinter import ttk
from converter import Converter
import tkinter as tk

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window
        self.title("Currency Converter")
        self.geometry("400x400")
        self.config(bg="#283747")
        self.resizable(False, False)
        self.rates=Converter.get_currencies(self)

        # 'From' & 'To' Labels
        self.from_currency = Label(
            self, 
            text="From", 
            bg="#283747", 
            fg="white", 
            font=("franklin gothic medium", 15)
            )

        self.from_currency.place(
            x=75, 
            y=50, 
            anchor="center"
            )

        self.to_currency = Label(
            self, 
            text="To", 
            bg="#283747", 
            fg="white", 
            font=("franklin gothic medium", 15)
            )

        self.to_currency.place(
            x=325, 
            y=50, 
            anchor="center"
            )

        # 'From' & 'To' Entry Boxes
        self.from_currencies = StringVar(self)
        self.from_currencies.set("USD")

        self.from_box = ttk.Combobox(
            self,
            width=20,
            textvariable=self.from_currencies,
            values=list(self.rates),
            state="readonly"
            )

        self.from_box.place(
            x=75, 
            y=75, 
            anchor="center"
            )

        self.to_currencies = StringVar(self)
        self.to_currencies.set("EUR")

        self.to_box = ttk.Combobox(
            self,
            width=20,
            textvariable=self.to_currencies,
            values=(list(self.rates)),
            state="readonly",
            )

        self.to_box.place(
            x=325,
            y=75,
            anchor="center"
            )

        # Amount Label & Entry Box
        self.amount = Label(
            self, 
            text="Amount", 
            bg="#283747", 
            fg="white", 
            font=("franklin gothic medium", 15))

        self.amount.place(x=200, y=125, anchor="center")

        self.amount_box = Entry(self)
        self.amount_box.config(width=30)
        self.amount_box.place(x=200, y=150, anchor="center")
