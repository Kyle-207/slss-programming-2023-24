# Parental Bot
# Author: Kyle Wang
# Nov 14, 2023

# Create 4 questions for the parental bot

questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"
    ]

# When the user answers "yes", user's points will increase by 1

points = 0

for question in questions:
    print(question)
    answer = input().lower().strip(",.?/! ")

    if answer == "yes":
        points += 1

# At the end, reply to the user depending on the points the user has

if points >= 1 and points <= 2:
    print("Ok.")
elif points >= 3 and points <= 4:
    print("Good!")
elif points == 0:
    print("I'm coming over.")