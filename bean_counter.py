# Bean Counter
# Author: Kyle Wang
# 9 January 2024

from colour_helper import pixel_to_string

from PIL import Image

RED_PIXEL = (150, 0, 0)
GREEN_PIXEL = (80, 30, 30)
PURPLE_PIXEL = ()

# Version 0.1
# Count all red pixels
# Report on the percentage of all red

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []
purple_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        current_pixel = jelly_bean_img.getpixel((x, y))

        # If that pixel is red, store the location
        if pixel_to_string(current_pixel) == "red":
            red_pixels.append((x, y))
        elif pixel_to_string(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))
        elif pixel_to_string(current_pixel) == "purple":
            purple_pixels.append((x, y))

# Display the number of pixels of each colour has 
print(len(green_pixels))
print(len(red_pixels))
print(len(purple_pixels))

# Calculate the percentage of all jelly bean colours
# Divide that number by the total pixels in the image
original_size = (jelly_bean_img.height, jelly_bean_img.width)

red_percentage = len(red_pixels) / (jelly_bean_img.height * jelly_bean_img.width) * 100
green_percentage = len(green_pixels) / (jelly_bean_img.height * jelly_bean_img.width) * 100
purple_percentage = len(purple_pixels) / (jelly_bean_img.height * jelly_bean_img.width) * 100

# Display report
print(f"Red Jelly Beans: {round(red_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_percentage, 2)}%")
print(f"Purple Jelly Beans: {round(purple_percentage, 2)}%")

# Create a map of all red pixels
# Create a new image that is the same size as the original image

red_pixel_map = Image.new("RGB", original_size)

# For every pixel location in "found" pixel list, place a pixel on that image

for pixel_loc in red_pixels:
    red_pixel_map.putpixel(pixel_loc, RED_PIXEL)

for pixel_loc in green_pixels:
    red_pixel_map.putpixel(pixel_loc, GREEN_PIXEL)

for pixel_loc in purple_pixels:
    red_pixel_map.putpixel(pixel_loc, PURPLE_PIXEL)

red_pixel_map.save("colours_pixel_map.jpg")


red_pixel_map.close()
jelly_bean_img.close()

# Version 0.1 ---
# Count all red pixels
# Report on the percentage of all red jellybeans
# Version 0.2 ---
# Count all green pixels
# Report on the percentage of all green jellybeans
# Version 0.3 ---
# Count all purple pixels
# Report on the percentage of all purple jellybeans