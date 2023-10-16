# Star Wars Bot
# Author: Kyle Wang
# Oct 16, 2023

import time

# Introduce the bot

print("Hello, I am a Star Wars Bot. I can decide if you are on the Dark side or not.")
time.sleep(0.5)
print("There are two questions that you need to answer.")

# Ask if the user likes the colour red or capes

like_red = input("Do you like the colour red?").lower()
time.sleep(1)

like_capes = input("Do you like capes?").lower()
time.sleep(1)

# Decide if the user is on the Dark side or the Light side

if like_red == "yes" or like_capes == "yes":
    print("Dark side it is!")

elif like_red == "no" and like_capes == "no":
    print("Light side, I see.")

else:
    print("Light side, I see.")