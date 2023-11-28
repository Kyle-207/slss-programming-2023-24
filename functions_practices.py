# Functions Practice
# Author: Kyle Wang
# 24 November 2023

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square
	"""
    area = sidelength**2
	
    return area

    

def print_area_of_a_square(sidelength: float) -> None:
	"""Calculate and print the area of a square.
	Results are in units squared.

	Params:

	sidelenth - length of one side of the square
	"""
	area = sidelength**2
	
	print(f"The area of a square with side length {sidelength} is: {area} square units.")

print(print_area_of_a_square(12.2))
# print_area_of_a_square(12)

# Given two squares of two sidelengths
#       12.2 and 144
# Add the area of both squares

area_of_a_square = area_of_a_square(12.2) + area_of_a_square(144)
print(area_of_a_square)


# Question 1 - stars()
# Create a function called stars()
# Takes an int as a parameter
# Returns a string of stars of given length
def stars(x: int) -> str:
    """Returns a string of stars with the same length as the argument.
    
    Params:
    
    x - the number of stars in a string
    """
    output = "*" * x

    return output

print(stars(10))


# Question 2 - biggest_of_three()
# Create a function called biggest_of_three()
# Takes three parameters, all floats
# Returns the biggest one
def biggest_of_three(x: float, y: float, z: float) -> float:
    """Takes three numbers and returns the biggest of the three
     
    Params:
    
    x - the first number
    y - the second number
    z - the third number
    """
    
    if x > y and x > z or x == y and x > z or x == z and x > y:
         return x
    elif y > x and y > z or y == z and y > x:
         return y
    elif z > x and z > y:
         return z
    elif x == y == z:
         return x

print(biggest_of_three(67, 68, 69))



# Question 3 - pyramid()
# Takes one num as a parameter
# Give a pyramid either regular way or mirrored
def pyramid(x: int) -> None:
    """Creates a pyramid of stars
     
    Params:
      
    x - the num of the layers of the pyramid, which
    also equals the num of stars of the bottom layer
    """
    for i in range(1, x + 1):
        print(stars(i))

pyramid(10)

# Question 4 - pyramid_mirror()
def pyramid_mirror(x: int) -> None:
    """Creates a pyramid of stars, but mirrored
     
    Params:
      
    x - the num of the layers of the pyramid, which
    also equals the num of stars of the bottom layer
    """
    for i in range(1, x + 1):
        print(" " * (x-i) + stars(i))

pyramid_mirror(10)


