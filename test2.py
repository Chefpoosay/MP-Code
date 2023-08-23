import tkinter as tk
from PIL import Image, ImageTk
import base64
import io

def open_image():
    
    with open("info.txt", "r", encoding="utf-8") as file:
        image_data = file.read()

    image_bytes = base64.b64decode(image_data)

    image_stream = io.BytesIO(image_bytes)
    
    image = Image.open(image_stream)

    
    image.show()

root = tk.Tk()
root.withdraw()  

open_image()