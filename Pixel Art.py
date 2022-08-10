from PIL import Image

import os

files = os.listdir()
files.sort()
for i in files:
    if i != "Pixel Art.py":
        print(i)
        my_image = Image.open(i)
        pixel_art = my_image.resize((16,16), Image.Resampling.BILINEAR)
        image = pixel_art.resize((100, 100), Image.Resampling.NEAREST)
        image.save(i)
