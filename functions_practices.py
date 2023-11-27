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
def stars(x: int) -> str:
    """Returns a string of stars with the same length as the argument.
    
    Params:
    
    x - the number of stars in
    """
    output = "*" * x

    return output

print(stars(10))


# Question 2 - biggest_of_three()
def biggest_of_three(x: float, y: float, z: float) -> float:
    """Takes three numbers and returns the biggest of the three
     
    Params:
    
    x, y, z - the three numbers
    """
    
    if x > y and x > z or x == y and x > z or x == z and x > y:
         biggest = x
    elif y > x and y > z or y == z and y > x:
         biggest = y
    elif z > x and z > y:
         biggest = z
    elif x == y == z:
         biggest = x
         
    return biggest

print(biggest_of_three(67, 68, 69))


# Question 3 - pyramid()
def pyramid(x: int) -> str:
    """Creates a pyramid of stars
     
    Params:
      
    x - the num of the layers of the pyramid, which
    also equals the num of stars of the bottom layer
    """
    for i in range(1, x + 1):
        output = print("*" * i)

    return output

pyramid(10)

# Question 4 - pyramid_mirror()
def pyramid_mirror(x: int) -> str:
    """Creates a pyramid of stars, but mirrored
     
    Params:
      
    x - the num of the layers of the pyramid, which
    also equals the num of stars of the bottom layer
    """
    for i in range(1, x + 1):
        output = print(" " * (x-i) + "*" * i)

    return output

pyramid_mirror(10)


