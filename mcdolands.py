# McDoland's
# Author: Kyle Wang
# 3 Nov 2023

import time

# Greet the user

print("Hi, this is the McDoland's ordering program, you can order some food here.")

# Ask if the user would like a burger and/or fries

need_burger = input("Would you like a burger for $5? (Yes / No)")
need_fries = input("Would you like fries for $3? (Yes / No)")

time.sleep(1)

order_cost = 0

if need_burger.lower().strip(",.?!/ ") == "yes":
    order_cost += 5

if need_fries.lower().strip(",.?!/ ") == "yes":
    order_cost += 3

# Calculate the total money with a 14% tax

tax_rate = 0.14         # 14%

final_cost = round(order_cost * (1 + tax_rate), 2)

# Print out the total to the user

print(f"Your total is ${final_cost}")
