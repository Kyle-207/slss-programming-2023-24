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


    if g > 220 and r < 120 and b < 120:
        return "green"
    
    # TODO: Implement detecting the colour red
    if g < 25 and r > 140 and b < 25:
        return "red"
    
    if g >= 80 and b < 40 and r <= 65:
        return "jelly bean green"
    
    if g <= 110 and b > 90 and r >= 40 and r < 150:
        return "purple"
    
    if r >= 159 and g < 80 and b <= 85:
        return "red ball"

# Question 1
    
def is_light(pixel: tuple) -> bool:
    """Take a rgb 3-tuple. If the average 
    is greater than or equal to 128, 
    return True, if not, return False.

    Params: 
        pixel - 3-tuple of (red, green, blue)
        
    Return:
        Boolean value according to the average
    """

    r, g, b = pixel

    if ((r + g + b) / 3) >= 128:
        return True
    else:
        return False
    
black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
white_pixel = (255, 255, 255)

print(is_light(black_pixel))      # False
print(is_light(dark_gray_pixel))  # False
print(is_light(light_gray_pixel)) # True
print(is_light(white_pixel))      # True


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Returns a grayscale version of the given pixel"""
    gray = int(pixel[0] * 0.3 + pixel[1] * 0.59 + pixel[2] * 0.11)

    return (gray, gray, gray)
