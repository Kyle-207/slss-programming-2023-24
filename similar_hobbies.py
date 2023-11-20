# Similar Hobbies
# Author: Kyle Wang
# Nov 14, 2023

# Get the hobbies from two different users

user_1_h = input("User 1, please enter your hobbies, separated by spaces. Please use underscores to replace with spaces.")
user_2_h = input("User 2, please enter your hobbies, separated by spaces. Please use underscores to replace with spaces.")

print(f"User 1: {user_1_h}")
print(f"User 2: {user_2_h}")

# Create a similarity score for the hobbies they have in common

sim_score = 0

# Compare the hobbies and count the sim score

for hobby in user_1_h.lower().strip(",./?!").split(" "):
    if hobby in user_2_h.lower().strip(",./?!").split(" "):
        sim_score += 1

# Print out the sim score

if sim_score == 1:
    print(f"You two have {sim_score} hobby in common!")
else:
    print(f"You two have {sim_score} hobbies in common!")