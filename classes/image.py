import customtkinter as ctk
import requests
import io
from PIL import Image as Img

class CustomImage(ctk.CTkLabel):
    def __init__(self, parent, img_source, padx=(0,0), pady=(0,0)):
        # Fetch Image From URL
        response = requests.get(img_source)
        image_data = io.BytesIO(response.content)
        
        # Open the image with PIL
        pil_image = Img.open(image_data)
        width, height = pil_image.size

        # Convert the PIL image for Tkinter
        tk_image = ctk.CTkImage(light_image=pil_image,
                                  dark_image=pil_image,
                                  size=(width * 1.4, height * 1.4))
        super().__init__(parent, image=tk_image, text="")

        self.pack(padx=padx, pady=pady)