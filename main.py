from converter import Converter
from menu import Menu
from tkinter import mainloop

if __name__ == "__main__":
    converter = Converter("USD", "EUR", 150)
    menu = Menu()

    mainloop()