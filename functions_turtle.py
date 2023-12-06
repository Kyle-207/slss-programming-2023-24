# Functions Turtle
# Author: Kyle Wang
# 28 November 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")

def squared(x: float) -> float:
    """Takes a num and squares it and returns it"""

    return x ** 2

def draw_square(x: int) -> None:
    burt.fd(x)
    burt.lt(90)
    burt.fd(x)
    burt.lt(90)
    burt.fd(x)
    burt.lt(90)
    burt.fd(x)
    burt.lt(90)

def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels
    
    Params:
    
    level - a num representing the levels of branches
    height - height of the main trunk in pixels
    """
    
    if level > 0:
        # 1. Move turtle forward height pixels
        burt.fd(height)

        # 2. Turn turtle left
        burt.lt(45)
        #   a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 3/4)

        # 3. Turn turtle right
        burt.rt(90)
        #   a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 3/4)

        # 4. Return to beginning
        burt.lt(45)
        burt.bk(height)
    else:
        original_color = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_color[0])


def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels
    
    Params:
    
    level - a num representing the levels of branches
    height - height of the main trunk in pixels
    """
    
    if level > 0:
        # 1. Move turtle forward height pixels
        burt.fd(height)

        # 2. Turn turtle left
        burt.lt(36)
        #   a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 3/4)

        # 3. Turn turtle right
        burt.rt(45)
        #   a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 3/4)
        burt.rt(44)

        #   b. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 3/4)

        # 4. Return to beginning
        burt.lt(53)
        burt.bk(height)
    else:
        original_color = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_color[0])


# Set up Burt to draw trees
burt.color('brown')
burt.setheading(90)     # points Burt north
burt.width(4)           # thicker trunk and branches
burt.speed(0)

draw_fancy_tree(2, 120)


turtle.done()

