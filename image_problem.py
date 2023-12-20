# Solutions to the image problems
# Author: Kyle Wang
# Dec 20 2023

import colour_helper

from PIL import Image

# Question 1




# Question 2: Binarizing an image
def binarize(filename: str) -> None:
    # Open the image
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                if colour_helper.is_light(pixel):
                    # replace with white pixel
                    im.putpixel((x, y), colour_helper.white_pixel)
                else:
                    # replace with black pixel
                    im.putpixel((x, y), colour_helper.black_pixel)
        
        im.save("./Images/binarized_image.jpg")
    
binarize("output.jpg")

# Extension problem

def image_to_grayscale(filename: str) -> None:
    """Convert an image to grayscale"""
   
    with Image.open(f"./Images/{filename}") as im:
        for y in range (im.height):
            for x in range (im.width):
                pixel = im.getpixel((x, y))

                im.putpixel((x, y), colour_helper.pixel_to_grayscale(pixel))

        im.save("./Images/grayscale.jpg")

image_to_grayscale("best_pizza.jpg")