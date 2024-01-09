# Winter Holidays
# Author: Kyle Wang
# 8 January 2024

import random

# Requirements:
#  - Create a funcation called winter_holiday()
#       - takes one parameter - string
#       - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

good_response = ["I slept a lot.",
                 "I went to Aberdeen Centre and saw a huge bear for Christmas decorations.",
                 "I finished reading a book."]
bad_response  = ["I played too much video games.",
                 "I gave up doing math."]


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter 
    holidays 2023/24

    Params:
    good_or_bad - string that indicates whether the event
    is good or bad

    Returns:
        an event that happened to you during the holidays 
        the event is selected part"""
    # if the response is good, return an event from good_response list
    if good_or_bad.lower().strip(",.?/!") == "good":
        return random.choice(good_response)
    
    # if the response is bad, return an event from bad_response list
    elif good_or_bad.lower().strip(",.?/!") == "bad":
        return random.choice(bad_response)


def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    print(winter_holiday("bad"))

if  __name__ == "__main__":
    main()
