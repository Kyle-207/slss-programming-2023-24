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

draw_square(50)

burt.speed(0)
burt.penup()
burt.goto(-200,-200)
burt.pendown()
# Draw squares that grow exponentially
for i in range(25):
    draw_square(squared(i))


turtle.done()