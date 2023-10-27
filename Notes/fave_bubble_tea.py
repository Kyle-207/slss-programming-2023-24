# Bubble Tea Popularity Algorithm
# Author: Kyle Wang
# Oct 27, 2023

# Ask 5 users what their favourite bubble tea place is
# Prints out a summary of the data

# Like counters
coco_likes = 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

# ------ CONSTANTS
NUM_RESPONDENTS = 5

# ------

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    # Store that information somewhere
    print("What's your favourtite bubble tea place?")

    fave_place = input().strip(",.?!").lower()

    # Tally or counting algo
    # Options: CoCo, Suntea, Chatime, Bubble Queen
    # If they choose any of these options, increase the counter
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1



# Repeat the code above 5 times


# Print out a summary
print(f"Coco Likes: {coco_likes}, which is {coco_likes / NUM_RESPONDENTS * 100}%")
print(f"Suntea Likes: {suntea_likes}, which is {suntea_likes / NUM_RESPONDENTS * 100}%")
print(f"Chatime Likes: {chatime_likes}, which is {chatime_likes / NUM_RESPONDENTS * 100}%")
print(f"Bubble Queen Likes: {bubqueen_likes}, which is {bubqueen_likes / NUM_RESPONDENTS * 100}%")