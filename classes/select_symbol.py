from datetime import datetime

import customtkinter as ctk

from classes.border_container import BorderContainer
from classes.image import CustomImage as Image
from colors import *


class SelectSymbol(BorderContainer):
    def __init__(self, parent, client, setter):
        super().__init__(
            parent,
            title=" 1. Select Symbol ",
            fg_color=background_color,
            side="left",
            fill="both",
            expand=True,
        )

        # 1st Section To Display Exchange Visa
        logo_text1 = ctk.CTkLabel(
            self.frame,
            text="Selected Exchange",
            font=main_font_bold,
            text_color=font_color,
        )
        logo_text1.pack(pady=(16, 0))
        Image(self.frame, client.current.urls["logo"], pady=(4, 0))
        logo_text2 = ctk.CTkLabel(
            self.frame,
            text="Change the exchange in the menu.",
            font=title_font,
            text_color=warning_color,
        )
        logo_text2.pack()

        # 2nd Section To Display Combo Input For The Base Currency
        self.symbol_base = None

        self.main_symbol_base = ctk.CTkComboBox(
            self.frame,
            width=168,
            height=32,
            values=client.base_markets,
            font=main_font_bold,
            fg_color=button_color,
            border_color=button_color,
            button_color=primary_color,
            button_hover_color=primary_hover_color,
            dropdown_fg_color=button_hover_color,
            dropdown_hover_color=primary_color,
            dropdown_font=main_font,
            dropdown_text_color=(button_color[1], button_color[0]),
            command=lambda value: self.select_symbol_base(value, client),
        )
        self.main_symbol_base.set("Select Base Token")
        self.main_symbol_base.pack(pady=(16, 0))

        # 3rd Section To Display Combo Input For The Full Symbol
        self.main_symbol_pair = ctk.CTkComboBox(
            self.frame,
            width=168,
            height=32,
            values=[],
            font=main_font_bold,
            fg_color=button_color,
            border_color=button_color,
            button_color=primary_color,
            button_hover_color=primary_hover_color,
            dropdown_fg_color=button_hover_color,
            dropdown_hover_color=button_color,
            dropdown_font=main_font,
            dropdown_text_color=(button_hover_color[1], button_hover_color[0]),
            state="disabled",
            command=lambda value: self.selected_symbol(value, setter, client),
        )
        self.main_symbol_pair.set("Select Pair")
        self.main_symbol_pair.pack(pady=(8, 0))

        # Display The Chosen Symbol In Text
        select_symbol_frame = ctk.CTkFrame(self.frame, fg_color=background_color)
        select_symbol_frame.pack()

        self.selected_symbol_is_label = ctk.CTkLabel(
            select_symbol_frame, font=main_font, text=""
        )
        self.selected_symbol_is_label.pack(side="left")
        self.selected_symbol_label = ctk.CTkLabel(
            select_symbol_frame, font=main_font_bold, text=""
        )
        self.selected_symbol_label.pack(side="left")

    def select_symbol_base(self, value, client):
        self.symbol_base = value
        symbol_pairs = [
            element for element in client.markets if element.startswith(value + "/")
        ]

        self.main_symbol_pair.configure(state="normal", values=symbol_pairs)
        self.main_symbol_pair.set("Select Symbol")

    def fetch_first_available_date(self, client, start_date_str="2012-01-01"):
        start_date = client.current.parse8601(start_date_str + "T00:00:00Z")

        limit = 1000
        now = client.current.milliseconds()
        first_available_date_str = "No data found"

        while start_date < now:
            try:
                ohlcv = client.current.fetch_ohlcv(
                    self.symbol_pair, "1d", since=start_date, limit=limit
                )
                if ohlcv:
                    # Found data, get the first candle's timestamp and convert to "DD-MM-YYYY"
                    first_available_date_str = datetime.utcfromtimestamp(
                        ohlcv[0][0] / 1000
                    ).strftime("%d-%m-%Y")
                    print(f"First available date: {first_available_date_str}")
                    date = first_available_date_str.split("-")
                    return (int(date[2]), int(date[1]), int(date[0]))
                else:
                    # No data found, adjust start_date to search further ahead
                    start_date += (
                        86400000 * limit
                    )  # Increment start_date by 'limit' days in milliseconds
            except Exception as e:
                print(f"Error fetching data: {str(e)}")
                break  # Break out of the loop in case of an error

        return first_available_date_str

    def selected_symbol(self, value, setter, client):
        self.symbol_pair = value
        self.selected_symbol_is_label.configure(text="Selected: ")
        self.selected_symbol_label.configure(text=value)

        client.current.first_available_date = self.fetch_first_available_date(client)
        if client.current.first_available_date == "No data found":
            print("SOMETHINGS WRONG WITH THE DATE FETCHING HERE")
        setter()
