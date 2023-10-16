# Star Wars Bot
# Author: Kyle Wang
# Oct 16, 2023

import time

# Introduce the bot

print("Hello, I am a Star Wars Bot. I can decide if you are on the Dark side or not.")
time.sleep(0.5)
print("There are two questions that you need to answer.")

# Ask if the user likes the colour red or capes

answer_1 = input("Do you like the colour red?").lower()
time.sleep(1)

answer_2 = input("Do you like capes?").lower()
time.sleep(1)

# Decide if the user is on the Dark side or the Light side

if answer_1 == "yes" or answer_2 == "yes":
    print("Dark side it is!")

elif answer_1 == "no" and answer_2 == "no":
    print("Light side, I see.")

else:
    print("Light side, I see.")