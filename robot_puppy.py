# Robot Puppy
# Author: Kyle Wang
# 12 January 2024

from PIL import Image

from colour_helper import pixel_to_string

RED_PIXEL = (244, 59, 65)

ball_pixels = []

red_ball_img = Image.open("./Images/red_ball_360.jpg")

for y in range(red_ball_img.height):
    for x in range(red_ball_img.width):
        current_pixel = red_ball_img.getpixel((x, y))
                
        # Identify where the ball is in the image
        if pixel_to_string(current_pixel) == "red ball":
            ball_pixels.append((x, y))

# Create an image that can check if the right pixels are selected
original_size = (red_ball_img.width, red_ball_img.height)

ball_map = Image.new("RGB", original_size, color= (255, 255, 255))

for pixel_loc in ball_pixels:
     ball_map.putpixel(pixel_loc, RED_PIXEL)


ball_pixels.sort()
print(ball_pixels)

# Calculate the x, y location of the centre of the ball
centre_x = ((ball_pixels[-1][0]) - (ball_pixels[0][0]) + 1) // 2


ball_pixels.sort()
print(ball_pixels)

centre_y = ((ball_pixels))

ball_map.save("./Images/ball_map.jpg")

ball_map.close()
red_ball_img.close()

