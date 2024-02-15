import customtkinter as ctk
from colors import *

class Container(ctk.CTkFrame):
    def __init__(self, parent, width=None, height=None, fg=background_color,  corner_radius=0, expand=False, fill=None, padx=(0,0), pady=(0,0), side=None):
        # Configure frame options
        frame_options = {
            "master": parent,
            "fg_color": fg,
            "corner_radius": corner_radius,
        }
        if width is not None:
            frame_options["width"] = width
        if height is not None:
            frame_options["height"] = height

        # Initialize the frame with the specified options
        super().__init__(**frame_options)
        # Prevent the frame from automatically resizing to fit its contents
        if expand or fill is not None:
            self.pack_propagate(False)

        # Pack the frame into its parent with the specified layout options
        self.pack(side=side, expand=expand, fill=fill, pady=pady, padx=padx)