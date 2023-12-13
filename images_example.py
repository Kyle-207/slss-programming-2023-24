# Images and Python
# Author: Kyle Wang
# 11 December 2023

from PIL import Image

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name.

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel

    if g > 250 and r < 32 and b < 32:
        return "green"
    

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # Algorithm to visit every pixel in the kid-green image
    # Store the height and width of the image
    image_height = im.height
    image_width = im.width

    # outer loop is top to bottom
    # inner loop is left to right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x,y))
            
            # Detects green pixels
            if pixel_to_string(pixel) == "green":
                print("GREEN PiXEL!!!")
            else:
                print("UNKNOWN PIXEL!!!")
