# World Traveller Bot
# Author: Kyle Wang
# Nov 3 2023

# Greet the user and ask for their name

user_name = input("What is your name?").strip(",.?!/")

print(f"Hello, {user_name}! Nice to meet you. I am the World Traveller Bot that counts how many continents you've been to.")

# Ask if the user has been to each of the continents

continents = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]
con_counts = 0

for continent in continents:
    been_to_c = input("Have you been to" + continent + "? (Yes / No)")
    if been_to_c.lower.strip(",.?!/ ") == "yes":
        con_counts += 1

# When finished asking, tell the user how many continents they've been to. 

print(f"I see, you've visited {con_counts} / 7 continents.")