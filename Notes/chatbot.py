# Chatbot
# Author: Kyle Wang
# Date: 20 September 2023

# Greet the user
print("Hello there! 😄")
print("I'm a crude Chatbot, here to talk to you.")

# Get the user's name and store it in a variable
user_name = input("What is your name? or, Como se llama?")

# Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}.")

# Ask the user what their favourite food is
fave_food = input("Tell me a little bit about you, what's your favourite food?")


# Make a comment abou their food but NOT BE TERRIBLY REPETITIVE
# Create a list of possible responses
list_of_responses = [
    f"Oh. I've never had {fave_food} before.",
    "Mmmmmm. That sounds good!",
    "I heard that that is delicious.",
    "Cool."
    ]

# Choose one of those responses randomly
import random
random_food_response = random.choice (list_of_responses)

# Print out that chosen response
print(random_food_response)