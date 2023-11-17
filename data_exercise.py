from pathlib import Path


# File Exercises
# Author: Kyle Wang
# Nov 15, 2023

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.


with open("./data_example.csv", encoding="utf-8") as f:
     for line in f:
        list_of_data = line.split(",")

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.

ca_likes = 0

with open("./data_example.csv", encoding="utf-8") as f:
    for line in f:
        list_of_data = line.split(",")
        for item in list_of_data:
            if item == "Chicken Adobo":
                ca_likes += 1

print(f"There are {ca_likes} people who like Chicken Abodo.")
    


# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

first_letter = "A"

with open("./data_example.csv", encoding="utf-8") as f:
     header = f.readline()

    # Convert the data into a list
     for line in f:
        list_of_data = line.split(",")

        # Create a counter for the first letter that starts with "A"
        first_letter_count = 0
        # Store the current person's name
        first_names = list_of_data[0]

        # Create an algo that counts the num of people whose first names start with "A"
        for name in first_names:
        
            if first_names[0] == first_letter:
                first_letter_count += 1
        
        

print(f'There are {first_letter_count} people whose first letter of their first name start with "A".')
        


# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

# with open("./data_example.csv", encoding="utf-8") as f:
#      header = f.readline()

#     # Convert the data into a list
#      for line in f:
#         list_of_data = line.split(",")
        
#         city_count = 0
#         city_list = list_of_data[4]

#         for city in list_of_data[4]:
#             if city == "Guangshou":
#                 city_count += 1

#         print(list_of_data[4])
#         print(city)

# print(f"The number of people who come from Guangzhou: {city_count}")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.


# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?


