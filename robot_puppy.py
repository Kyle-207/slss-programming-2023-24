# Robot Puppy
# Author: Kyle Wang
# 12 January 2024

from PIL import Image

from colour_helper import pixel_to_string

def centre_of_the_ball(pixel_loc: tuple) -> tuple:
    """Identify the location of the ball in the image.
       Calculate the x, y location of the centre of the 
       ball in the image.
       
       Params:
            pixel_loc - get the x, y location of the pixels of the ball
            
        Returns:
            the x, y location of the centre of the ball"""
    
    # 