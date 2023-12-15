# Colour Helper
# Author: Kyle Wang
# 13 December 2023

# Do you need help with colours
# This is for you

def pixel_to_string(pixel: tuple) -> str:
    """Take a rgb 3-tuple and "interpret it"
    as a colour and return that colour's name.

    Params:
        pixel - 3-tuple of (red, green, blue)

    Return:
        String representing the colour
    """
    r, g, b = pixel


    if (g > 224 and r < 57 and b < 81) or (g > 186 and r < 53 and b < 156) or (g > 163 and r < 124 and b < 43):
        return "green"
    elif (g > 172 and r < 75 and b < 91) or (g > 134 and r < 101 and b < 32):
        return "green"