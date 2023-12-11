# Images and Python
# Author: Kyle Wang
# 11 December 2023

from PIL import Image

# Recall that we can open up files in Python
with Image.open("kid-green.jpg") as f:
    f.readline()