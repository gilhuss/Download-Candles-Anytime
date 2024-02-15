import customtkinter as ctk

from classes.client import Client
from classes.container import Container
from classes.download_selection import DownloadSelection
from classes.header import Header
from classes.menu import Menu
from classes.select_symbol import SelectSymbol
from classes.select_timeframe import SelectTimeframe
from colors import *


class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Create The CCXT Client
        self.client = Client()

        # Create The Menu
        self.menu = Menu(
            self,
            self.client.exchanges,
            self.change_exchange,
            self.load_ui,
        )
        self.config(menu=self.menu)

        # Update Client
        self.client.set_client(self.menu.get_selected_exchange())

        self.body = Container(self, expand=True, fill="both", fg=header_color)
        self.header = Header(
            self.body, expand=False, fill="x", height=56, fg=header_color
        )
        self.main = Container(self.body, expand=True, fill="both")

        self.load_ui()

    def change_exchange(self):
        # Update Function For The Client
        exchange_name = self.menu.get_selected_exchange()
        self.client.set_client(exchange_name)
        self.load_ui()

    def load_ui(self):
        # Reload The Current UI
        self.delete_widgets(["first_main", "second_main", "third_main"])
        # Creating/Reload UI
        self.first_main = SelectSymbol(
            self.main, self.client, self.set_symbol_completed
        )

        self.second_main = SelectTimeframe(
            self.main,
            self.client,
            self.set_timeframe_completed,
        )
        self.third_main = DownloadSelection(self.main)

    def set_symbol_completed(self):
        self.second_main.main_timeframe.configure(
            state="normal", values=list(self.client.timeframes.values())
        )
        self.second_main.main_timeframe.set("Select Timeframe")

    def set_timeframe_completed(self, completed):
        if completed:
            self.is_timeframe_completed = True
            self.third_main.set_selection(
                client=self.client.current,
                pair=self.first_main.symbol_pair,
                timeframe=self.second_main.timeframe,
                start=self.second_main.start_value,
                end=self.second_main.end_value,
                reset=self.load_ui,
            )

    def delete_widgets(self, widgets):
        for widget in widgets:
            if hasattr(self, widget):
                widget_ = getattr(self, widget)
                widget_.destroy()
