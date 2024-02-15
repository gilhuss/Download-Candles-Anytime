import customtkinter as ctk

from classes.border_container import BorderContainer
from classes.button import Button
from classes.calendar import Calendar_
from classes.double_label import DoubleLabel
from colors import *


class SelectTimeframe(BorderContainer):
    def __init__(self, parent, client, setter):
        super().__init__(
            parent,
            title=" 2. Select Timeframes ",
            fg_color=background_color,
            side="left",
            fill="both",
            expand=True,
        )

        self.timeframe = None

        self.main_timeframe = ctk.CTkComboBox(
            self.frame,
            width=168,
            height=32,
            font=main_font_bold,
            fg_color=button_color,
            border_color=button_color,
            button_color=primary_color,
            button_hover_color=primary_hover_color,
            dropdown_fg_color=button_hover_color,
            dropdown_hover_color=primary_color,
            dropdown_font=main_font,
            dropdown_text_color=(button_color[1], button_color[0]),
            state="disabled",
            command=lambda value: self.select_timeframe(value, client),
        )
        self.main_timeframe.pack(pady=(16, 0))

        self.select_symbol_frame = ctk.CTkFrame(self.frame, fg_color=background_color)
        self.select_symbol_frame.pack()

        self.selected_timeframe_is_label = ctk.CTkLabel(
            self.select_symbol_frame, font=main_font, text=""
        )
        self.selected_timeframe_is_label.pack(side="left")
        self.selected_timeframe_label = ctk.CTkLabel(
            self.select_symbol_frame, font=main_font_bold, text=""
        )
        self.selected_timeframe_label.pack(side="left")

        # Display Start & End Periods
        calendar_title = ctk.CTkLabel(self.frame, text="Select Period")
        calendar_title.pack(pady=(16, 0))

        self.start_button = Button(
            self.frame,
            primary=True,
            text="Start Period",
            command=lambda: self.start_period(client.current, setter),
            state="disabled",
            pady=(8, 0),
        )

        self.end_button = Button(
            self.frame,
            primary=True,
            text="End Period",
            command=lambda: self.end_period(setter),
            state="disabled",
            pady=(8, 0),
        )

    def select_timeframe(self, value, client):
        value_key = ""
        for key, timeframe in client.timeframes.items():
            if value == timeframe:
                value_key = key

        self.timeframe = value_key
        self.selected_timeframe_is_label.configure(text="Selected: ")
        self.selected_timeframe_label.configure(text=value)
        self.start_button.configure(state="normal")

    def start_period(self, client, setter):
        self.start_value = ""

        def start():
            self.start_value = cal.cal.get_date()
            print(cal.cal.get_date())
            cal.destroy()
            display_text()

        def display_text():
            if hasattr(self, "end_display"):
                self.start_display.destroy()

            self.start_display = DoubleLabel(
                self.frame, texts=["Start: ", self.start_value]
            )
            self.end_button.configure(state="normal")
            if hasattr(self, "start_value") and hasattr(self, "end_value"):
                setter(True)

        cal = Calendar_(
            self.frame,
            title="Select Start Period",
            command=start,
            min=client.first_available_date,
        )

    def end_period(self, setter):
        self.end_value = ""

        def end():
            self.end_value = cal.cal.get_date()
            print(cal.cal.get_date())
            cal.destroy()
            display_text()

        def display_text():
            if hasattr(self, "end_display"):
                self.end_display.destroy()
            self.end_display = DoubleLabel(self.frame, texts=["End: ", self.end_value])
            if hasattr(self, "start_value") and hasattr(self, "end_value"):
                setter(True)

        cal = Calendar_(self.frame, title="Select End Period", command=end, today=True)
