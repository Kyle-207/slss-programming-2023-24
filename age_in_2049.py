# Age in 2049
# Author: Kyle Wang
# 1 November 2023

import time
import datetime

# Ask the user what their age is
# and store their response

user_age = int(input("I can calculate your age in 2049. How old are you?").strip(",.?! "))

# Do the math

x = datetime.datetime.now()

future_age = user_age + (2049 - x.year)

# Show the result to the user

print(f"You will be {future_age} years old in 2049.")