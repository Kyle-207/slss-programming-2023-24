# Winter Holidays
# Author: Kyle Wang
# 8 January 2024

import random

# Requirements:
#  - Create a funcation called winter_holiday()
#       - takes one parameter - string
#       - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

good_response = ["", "2", "3"]
bad_response  = [""]


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter 
    holidays 2023/24

    Params:
    good_or_bad - string that indicates whether the event
    is good or bad

    Returns:
        an event that happened to you during the holidays 
        the event is selected part"""
    if good_or_bad.lower().strip(",.?/!") == "good":
        return random.choice(good_response)
    
    elif good_or_bad.lower().strip(",.?/!") == "bad":
        return random.choice(bad_response)


def main() -> None:
    # Runs all the things we want to test in our .py file
    winter_holiday("good")

if  __name__ == "__main__":
    main()


print(winter_holiday("good"))
