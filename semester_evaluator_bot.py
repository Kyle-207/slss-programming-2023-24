# Semester Evaluator Bot
# Author: Kyle Wang
# 3 Nov 2023

# Ask how many courses the user is taking this semester

num_of_courses = input("Hello, I'm a semester evaluator. How many courses are you taking?").lower().strip(",.?/! ")

# For each course, it asks the user to rate the course out of 5

total_score = 0

for course in range(int(num_of_courses)):
    rate = input(f"How do you rate course {course + 1} from 1 to 5?").lower().strip(",./?! ")
    total_score += int(rate)

# Takes the average rating of the courses and gives a comment about the average.

average = round(total_score / int(num_of_courses), 1)

print(f"Your average courses rating is {average} out of 5.")

# Score: <= 1 -- Ouch
# Score: 1 < x < 3 -- Not a bad semester
# Score: > 3 -- <score>? Glad to hear that!

if average <= 1:
    print("That doesn't sound very pleasant. Ouch.")
elif average > 1 and average < 3:
    print(f"{average}? Not a bad semester.")
elif average > 3:
    print(f"{average}? Glad to hear that!")