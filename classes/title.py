import customtkinter as ctk
from colors import *

class Title(ctk.CTkLabel):
    def __init__(self, parent, text="", expand=False, fill=None, justify="left"):
        super().__init__(parent, text=text, text_color=font_color, justify=justify, fg_color="red")
        
        self.place(x=8, y=0, anchor="nw")
        