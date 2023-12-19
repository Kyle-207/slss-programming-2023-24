# Images and Python
# Author: Kyle Wang
# 11 December 2023

import colour_helper

from PIL import Image    

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # Algorithm to visit every pixel in the kid-green image
    # Store the height and width of the image
    image_height = im.height
    image_width = im.width

    # load the background image
    bg_im = Image.open("./Images/beach.jpg")

    # outer loop is top to bottom
    # inner loop is left to right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            # check pixel if it's green
            if colour_helper.pixel_to_string(pixel) == "green":
                # if it is, replace it with bg_img
                # pixel from the same coordinate    
                bg_pixel = bg_im.getpixel((x, y))
                im.putpixel((x, y), bg_pixel)
    bg_im.close()

    # save the image
    im.save("./Images/output.jpg")

    


# Question 2

with Image.open("./Images/best_pizza.jpg") as im:

    image_height = im.height
    image_width = im.width

    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))
            if colour_helper.is_light(pixel) == True:
                im.putpixel((x, y), colour_helper.white_pixel)
            else:
                im.putpixel((x, y), colour_helper.black_pixel)

    im.save("./Images/output2.jpg")

