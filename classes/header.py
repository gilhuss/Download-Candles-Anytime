import customtkinter as ctk
import darkdetect
from PIL import Image
from colors import *

class Header(ctk.CTkFrame):
    def __init__(self, parent, width=None, height=None, fg=background_color,  corner_radius=0, expand=False, fill=None, padx=(0,0), pady=(0,0)):
        # Configure frame options
        frame_options = {
            "master": parent,
            "fg_color": fg,
            "bg_color": header_color,
            "corner_radius": corner_radius,
        }
        if width is not None:
            frame_options["width"] = width
        if height is not None:
            frame_options["height"] = height

        # Initialize the frame with the specified options
        super().__init__(**frame_options)
        
        self.moon_image = ctk.CTkImage(Image.open("images/moon_dark.png"), size=(20, 20))
        self.sun_image = ctk.CTkImage(Image.open("images/sun_light.png"), size=(20, 20))

        self.theme = str(darkdetect.theme()).lower()
        self.theme_image = self.sun_image if self.theme == "dark" else self.moon_image
        self.theme_text = "Change to Light Mode" if self.theme == "dark" else "Change to Dark Mode"
        
        
        self.header_theme_label = ctk.CTkLabel(self, text = self.theme_text, font=main_font)
        self.header_theme_button = ctk.CTkButton(self, 
                                text = "",
                                width=40, 
                                height=40, 
                                corner_radius=4, 
                                fg_color=button_color, 
                                hover_color=button_hover_color,
                                text_color=font_color,
                                command=lambda: self.change_theme(self.header_theme_button, self.header_theme_label),
                                font=main_font,
                                image = self.theme_image
                                )

        self.header_theme_button.pack(side = "right", padx= 8)
        self.header_theme_label.pack(side = "right")

        self.header_label = ctk.CTkLabel(self, text = "DCA", font=header_font)
        self.header_label.pack(side="left", padx=12)
        
        # Prevent the frame from automatically resizing to fit its contents
        if expand or fill is not None:
            self.pack_propagate(False)

        # Pack the frame into its parent with the specified layout options
        self.pack(expand=expand, fill=fill, pady=pady, padx=padx)


    def change_theme(self, theme_button, theme_label):
        return_theme = "light" if self.theme == "dark" else "dark"
        self.theme = return_theme
        # Change Image of Button
        theme_image = self.sun_image if self.theme == "dark" else self.moon_image
        theme_button.configure(image=theme_image)
        # Change Text of Label
        theme_text = "Change to Light Mode" if self.theme == "dark" else "Change to Dark Mode"
        theme_label.configure(text=theme_text)
        # Change Theme
        ctk.set_appearance_mode(return_theme)