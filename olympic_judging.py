# Olympic Judging
# Author: Kyle Wang
# 1 November 2023

import time

# Greet the user

print("Hello, this is an Olympic Judging program. You'll need to input 5 scores, and I'll give you the average.")

# Get 5 scores for the user
judges = ["Judge 1", "Judge 2", "Judge 3", "Judge 4", "Judge 5"]

# Each is out of 10 points maximum
time.sleep(1)
print("Each score is out 10 points maximum, you can use half points if you want.")

final_score = 0

for judge in judges:
    score = float(input(judge + ": ").strip(",.?!/ "))
    if score >= 0 and score <= 10:
        final_score += score
    else:
        print("Your input score does not match the restrictions, please type again.")
        score = float(input(judge + ": ").strip(",.?!/ "))

# Calculate the average score

average_score = round(final_score / len(judges), 2)

# Print the average score to the user

time.sleep(1)
print(f"Your Olympic score is: {average_score} / 10")