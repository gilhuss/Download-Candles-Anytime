import tkinter as tk

from classes.label import Label
from classes.window import Window
from colors import *


class Menu(tk.Menu):
    def __init__(self, parent, exchanges, change_exchange, reset):
        super().__init__(parent)

        self.create_file_menu(parent, reset)
        self.create_exchanges_menu(exchanges, change_exchange)
        self.create_help_menu()

        parent.config(menu=self)

    def create_file_menu(self, parent, reset):
        file_menu = tk.Menu(self, tearoff=False, activeforeground=primary_color[1])

        file_menu.add_command(label="Reset", command=reset)
        file_menu.add_separator()
        file_menu.add_command(
            label="Tip Creator", command=lambda: self.tip_creator(parent)
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit")

        self.add_cascade(label="File", menu=file_menu)

    def create_exchanges_menu(self, exchanges, change_exchange):
        # StringVar to hold the selected exchange's name
        self.selected_exchange = tk.StringVar()
        self.selected_exchange.set(exchanges[0]["id"])

        # Creating a submenu for exchanges
        exchanges_menu = tk.Menu(self, tearoff=False)

        for exchange in exchanges:
            exchanges_menu.add_radiobutton(
                label=exchange["name"],
                value=exchange["id"],
                variable=self.selected_exchange,
                command=change_exchange,
            )

        self.add_cascade(label="Exchanges", menu=exchanges_menu)

    def create_help_menu(self):
        help_menu = tk.Menu(self, tearoff=False, activeforeground=primary_color[1])

        help_menu.add_command(label="What Are The Steps ?")
        help_menu.add_command(label="Why Is This Used ?")
        help_menu.add_command(label="Contact Dev")

        self.add_cascade(label="Help", menu=help_menu)

    def get_selected_exchange(self):
        return self.selected_exchange.get()

    def tip_creator(self, parent):

        window = Window(parent=parent, title="Tip For The Creator")
        label = Label(parent=window, text="Hi I'm Gil.", bold=True)
        label.pack(fill="both", pady=(16, 0), padx=12)
        label2 = Label(
            parent=window, text="If you enjoy my work and want to support it,"
        )
        label2.pack(fill="both", padx=12)
        label3 = Label(parent=window, text="you can find my ETH address here:")
        label3.pack(fill="both", padx=12)
        label4 = Label(
            parent=window, text="0x764C707201eD28B98cd53307Ed39F1283dB8e263", bold=True
        )
        label4.pack(fill="both", pady=(0, 16), padx=12)
