# SFU's Best
# Author: Kyle Wang
# 1 November 2023

# Load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open the file
with open("./data.csv") as f:
    # Read the first line of data
    f.readline()
    
# Create a "profile" for someone that shows their
# favourite places at SFU

profile = [
    "Starbucks",
    "Bamboo Garden",
    "Uncle Fatih's",
    "Guadalupe",
    "Subway"
]

# Initialize our top and least similarity scores and their name
top_sim_score = 0
top_sim_name = ""

least_sim_score = 100
least_sim_name = ""

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()

    # For every line of data in the file (string)
    for line in f:
         # Convert the line of data into a list
        current_likes = line.split(",")

        # Initialize the CURRENT sim score
        # store the current person's name
        current_sim_score = 0
        current_name = current_likes[1]
        
        # sim score algo
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # print the current sim_score
        print(f"{current_name} - Score: {current_sim_score}")

        # Update the top score if this is highest
        if current_sim_score > top_sim_score:
            top_sim_score = current_sim_score
            top_sim_name = current_name
            

with open("./data.csv") as f:
    # Throw away the header line
    header = f.readline()

    # For every line of data in the file (string)
    for line in f:
         # Convert the line of data into a list
        current_likes = line.split(",")

        # Initialize the CURRENT sim score
        # store the current person's name
        current_sim_score = 5
        current_name = current_likes[1]
        
        # sim score algo
        for item in profile:
            if item not in current_likes:
                current_sim_score -= 1

        # print the current sim_score
        # print(f"{current_name} - Score: {current_sim_score}")

        # Update the least score if this is highest
        if current_sim_score < least_sim_score:
            least_sim_score = current_sim_score
            least_sim_name = current_name


print("TOP SIMILAR PERSON!")
print(f"{top_sim_name} - Score: {top_sim_score}")

print("LEAST SIMILAR PERSON!")
print(f"{least_sim_name} - Score: {least_sim_score}")



