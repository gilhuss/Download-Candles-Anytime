import time
from datetime import datetime
from tkinter import filedialog

import customtkinter as ctk
import pandas as pd

from classes.border_container import BorderContainer
from classes.button import Button
from classes.double_label import DoubleLabel
from colors import *


class DownloadSelection(BorderContainer):
    def __init__(self, parent):
        super().__init__(
            parent,
            title=" 3. Download Selection ",
            fg_color=background_color,
            side="left",
            fill="both",
            expand=True,
        )
        self.pair = ""
        self.end = ""
        self.start = ""
        self.timeframe = ""

    def set_selection(self, client, pair, timeframe, start, end, reset):
        if hasattr(self, "ui"):
            self.ui.destroy()
        self.pair = pair
        self.timeframe = timeframe
        self.start = start
        self.end = end

        self.ui = ctk.CTkFrame(self.frame, fg_color=background_color)
        self.ui.pack()
        DoubleLabel(self.ui, texts=["Pair: ", self.pair], pady=(16, 0))
        DoubleLabel(self.ui, texts=["Timeframe: ", self.timeframe])
        DoubleLabel(self.ui, texts=["Start Period: ", self.start])
        DoubleLabel(self.ui, texts=["End Period: ", self.end])
        Button(
            self.ui,
            text="Start Download",
            primary=True,
            height=40,
            pady=(16, 0),
            command=lambda: self.start_download(
                self.frame,
                client,
                self.pair,
                self.timeframe,
                self.start,
                self.end,
                reset,
            ),
        )

    def start_download(self, parent, client, pair, timeframe, start, end, reset):
        print("START DOWNLOADING")

        def convert_date(date_str):
            return datetime.strptime(date_str, "%d-%m-%Y").strftime(
                "%Y-%m-%dT00:00:00Z"
            )

        def fetch_candles(symbol, timeframe, start_timestamp, end_timestamp):
            limit = 1000
            all_candles = []

            while start_timestamp < end_timestamp:
                candles = client.fetch_ohlcv(
                    symbol, timeframe, since=start_timestamp, limit=limit
                )

                if not candles:
                    break

                last_timestamp = candles[-1][0]
                all_candles.extend(candles)

                if last_timestamp == start_timestamp:
                    break

                start_timestamp = (
                    last_timestamp + client.parse_timeframe(timeframe) * 1000
                )
                time.sleep(client.rateLimit / 1000)

            return all_candles

        def candles_to_dataframe(candles):
            columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
            df = pd.DataFrame(candles, columns=columns)
            df["Date"] = pd.to_datetime(df["Date"], unit="ms")
            return df

        # Validate and convert string dates to timestamps
        try:
            start_timestamp = client.parse8601(convert_date(start))
            end_timestamp = client.parse8601(convert_date(end))
        except Exception as e:
            print(f"Error parsing dates: {e}")
            return

        if start_timestamp is None or end_timestamp is None:
            print(f"Invalid start or end date. Start: {start}, End: {end}")
            return

        # Fetch and process data
        candles = fetch_candles(pair, timeframe, start_timestamp, end_timestamp)
        df = candles_to_dataframe(candles)

        # Ask user where to save the CSV file
        file_path = filedialog.asksaveasfilename(
            parent=parent,
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile=str(client) + "_" + pair + "_" + timeframe,
        )

        if file_path:  # Check if a file path was selected
            df.to_csv(file_path, index=False)
            print(f"Candles data saved to {file_path}")
            reset()
        else:
            print("File save operation cancelled.")
