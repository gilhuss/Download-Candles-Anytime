from tkinter import ttk

import customtkinter as ctk

from colors import background_color


class Window(ctk.CTkToplevel):
    def __init__(self, parent, title):
        super().__init__(parent, fg_color=background_color)
        self.title(title)
        self.theme = 0 if ctk.get_appearance_mode().lower() == "light" else 1
        style = ttk.Style()
        style.theme_use("clam")
