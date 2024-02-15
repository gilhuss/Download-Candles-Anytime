import customtkinter as ctk

from colors import *


class Label(ctk.CTkLabel):
    def __init__(self, parent, text, bold=False, color=font_color):
        super().__init__(
            parent,
            text=text,
            fg_color=background_color,
            text_color=color,
            font=main_font_bold if bold else main_font,
            state="active",
        )
