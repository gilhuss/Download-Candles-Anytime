import customtkinter as ctk

from colors import *


class DoubleLabel(ctk.CTkFrame):
    def __init__(self, parent, texts, pady=(0, 0), padx=(0, 0)):
        super().__init__(parent, fg_color=background_color)
        self.pack(pady=pady, padx=padx)

        labels = []
        text_counter = 0
        for text in texts:
            text_counter += 1
            if text_counter % 2 == 0:
                label = ctk.CTkLabel(
                    self, text=text, text_color=font_color, font=main_font_bold
                )
            else:
                label = ctk.CTkLabel(
                    self, text=text, text_color=font_color, font=main_font
                )
            labels.append(label)

        for label in labels:
            label.pack(side="left")
