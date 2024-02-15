import customtkinter as ctk
from colors import *

class BorderContainer(ctk.CTkFrame):
    def __init__(self, parent, title="", width=None, height=None, fg_color=background_color,  corner_radius=0, expand=False, fill=None, padx=(8,8), pady=(8,8), outerpadx=(0,0), outerpady=(0,0), side=None):
        
        frame_options = {
            "master": parent,
            "fg_color": fg_color,
            "corner_radius": corner_radius
        }
        if width is not None:
            frame_options["width"] = width
        if height is not None:
            frame_options["height"] = height

        # Initialize the frame with the specified options
        super().__init__(**frame_options)
        self.pack_propagate(False)
        self.pack(expand=expand, side=side, fill=fill, padx=outerpadx, pady=outerpady)
        
        self.frame = ctk.CTkFrame(self, fg_color=fg_color, border_color=(button_color[1], button_color[0]), border_width=1, corner_radius=12)
        self.frame.pack(expand=True, fill="both", pady=pady, padx=padx)
        title = ctk.CTkLabel(self, text=title.upper(), font=title_font, text_color=(button_color[1], button_color[0]), justify="right")
        title.place(x=16, y=-6)