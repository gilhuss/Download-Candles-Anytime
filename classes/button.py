import customtkinter as ctk

from colors import *


class Button(ctk.CTkButton):
    def __init__(
        self,
        parent,
        text="",
        primary=False,
        corner_radius=4,
        width=None,
        height=32,
        command=None,
        font=main_font_bold,
        side=None,
        state="normal",
        padx=(0, 0),
        pady=(0, 0),
    ):
        frame_options = {
            "master": parent,
            "text": text.upper(),
            "fg_color": primary_color if primary else button_color,
            "hover_color": primary_hover_color if primary else button_hover_color,
            "text_color": font_color,
            "font": font,
            "corner_radius": corner_radius,
            "height": height,
            "cursor": "pointinghand",
            "state": state,
            "command": command,
        }
        if width is not None:
            frame_options["width"] = width

        super().__init__(
            **frame_options,
        )

        self.pack(side=side, padx=padx, pady=pady)
