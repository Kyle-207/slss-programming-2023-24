# Functions and Recursion
# Author: Kyle Wang
# December 6, 2023

def factorial(num: int) -> int:
    """Returns the result of the number's
    factorial using recursion
    
    Params:
        num - number we're calculating
        
    Returns:
        result
    """

    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num
    
print(factorial(10))

# Calculate factorial using iteration

# x = int(input())
# y = 1

# for i in range(x, 0, -1):
#     y *= i

# print(y)

def fib(n: int) -> int:
    """Calculate and return the nth
    Fibonacci number
    """

    if n in [1, 2]:
        return 1
    elif n > 2:
        return (fib(n-1) + fib(n-2))
    
print(fib(10))
