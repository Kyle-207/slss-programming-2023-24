# Pumpkin Drawing
# Author: Kyle Wang
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

turtle.title("Pumpkin Drawing")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# Left Eye
carver.setpos(-30, 20)
carver.dot(30)

# Right Eye
carver.shape("circle")
carver.pendown()
carver.setpos(30, 20)
carver.dot(30)

# Mouth

carver.penup()
carver.setpos(0, -50)
carver.pendown()

n=10
while n <= 40:
    carver.circle(n)
    n = n+5




turtle.done()