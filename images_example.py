# Images and Python
# Author: Kyle Wang
# 11 December 2023

from PIL import Image

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # get the pixel into 
    pixel = im.getpixel((0,0))
    print(pixel)
    