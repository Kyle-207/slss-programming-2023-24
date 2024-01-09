# Bean Counter
# Author: Kyle Wang
# 9 January 2024

from colour_helper import pixel_to_string

from PIL import Image



# Version 0.1
# Count all red pixels
# Report on the percentage of all red

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x,y))

        # If that pixel is red, store the location
        if pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))

# Count every red pixel in the list
print(red_pixels)
print(len(red_pixels))
# Divide that number by the total pixels in the image
red_percentage = round(len(red_pixels) / (jelly_bean_img.height * jelly_bean_img.width), 2)
print(red_percentage)
# def bean_counter(pixel: tuple) -> tuple

