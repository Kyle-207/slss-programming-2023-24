# Chip Rater
# Author: Kyle Wang
# 1 November 2023

# Interview people about their
# perception of how delicious chips are
# based on a set of questions
# In the end, we'll give an aggregate score.

import time

# Greet the user
print("Please answer the following questions based on the chip you just ate.")

# Create a list of questions to ask
questions = [
    "How crispy is the chip on a scale from 1 to 5. 5 is very crispy. 1 is mushy.",
    "How would you ratre the taste from 1 to 5. 5 is the best taste ever. 1 is I would rather eat dirt.",
    "From 1 to 5, how would you rate the packaging? 5 is I would buy this JUST for the packing. 1 is someone got paid to put this together?"
    ]
final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)

    # Store their response
    rating = int(input().strip(",.?! "))
    final_score += rating


# Do some math - average
average_score = final_score / len(questions)

# Present the results to the user


print(f"The average score of this chip is: {average_score:.2f} / 5")

if average_score > 5:
    time.sleep(1)
    print("Wow! More than 5 points! You must be lovin' your chip.")
elif average_score <= 1:
    time.sleep(1)
    print("Hum... Better luck in finding the chip you love next time.")
