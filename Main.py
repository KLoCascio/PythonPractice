# # WEIRD/NOTWEIRD ELSEIF
# # Given an integer, , perform the following conditional actions:

# # If  is odd, print Weird
# # If  is even and in the inclusive range of  to , print Not Weird
# # If  is even and in the inclusive range of  to , print Weird
# # If  is even and greater than , print Not Weird

# import math
# import os
# import random
# import re
# import sys

# def weirdo(n: int) -> None:
#     if (n%2 !=0):
#         print("Weird")
#     elif (n%2==0 and 6<=n<=20):
#         print("Weird")
#     else:
#         print("Not Weird")

# if __name__ == '__main__':
#     n = int(input().strip())
#     weirdo(n)
    
# # DIVISION INTEGER/FLOAT
# # The provided code stub reads two integers, a and b, from STDIN.
# # Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.
# # No rounding or formatting is necessary.

# class Division:
#     def __init__(self, a, b):
#         # integer division
#         self.integer_results = a // b
#         # float division
#         self.float_results = a / b

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
#     division_instance = Division(a, b)
    
#     print(division_instance.integer_results)
#     print(division_instance.float_results)

# # INTRO https://github.com/SEIR-0911/u4_lesson_python_intro/tree/main
# # Execute Python scripts
# # Define and use variables
# # Create comments
# # Describe Python data types
# # Use and format Strings

# # Everything is an object. Stricly OOP.
# # Utilize snake_case and doesn't require let/const to declare variables

# # Create a variable for your name, string.
# users_name = "Kyndal"

# # Create a variable for number of items, integer.
# years_old = 30

# # Create a variable for completed, boolean.
# awesome = True

# # Create a variable for items, none.
# items = None

# print(users_name)
# print(years_old)
# print(awesome)
# print(items)
# print(10-1)

# # modulus vs division
# for i in range(10):
#     print (i//3, i%3)

# a = 10
# b = 6

# print(a//b, a%b)

# hours_in_day = 24
# days_in_year = 365

# # f-string interpolation
# msg = f'There are {hours_in_day} hours in a day, and {days_in_year} days in a year. The total hours in a year is {hours_in_day * days_in_year} hours.'

# # string format method
# template = "There are {} hours in a day, and {} days in a year."
# print(template.format(24, 365))

# print(msg)

# # To convert one data type into another, Python provides us with several global functions or predefined classes to do so:
# # str(item)        # Converts item to a string
# # int(item, base)  # Converts the provided item to an integer with the provided base
# # float(item)      # Converts the item to a floating-point number
# # hex(int)         # Converts an integer to a hexadecimal STRING
# # oct(int)         # Converts an integer to an octal STRING
# # tuple(item)      # Converts item to a tuple
# # list(item)       # Converts item to a list
# # dict(item)       # Converts item to a dictionary

# # PYTHON FUNCTIONS https://github.com/SEIR-0911/u4_lesson_python_functions
# # Compare Python to JavaScript functions
# # Define functions in Python
# # Invoke functions in Python

# def say_hello():
#     print('Hello!')

# say_hello()

# def do_math():
#     my_age = 30
#     weeks_in_year = 52
#     my_age_in_weeks = my_age * weeks_in_year
#     print(f'I am {my_age_in_weeks} weeks old.')

# do_math()

# # arguments/parameters

# def add_nums(num1, num2):
#     print(num1 + num2)

# add_nums(30, 40)

# # Lambda, similar to Arrow Functions in JS

# nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28]
# odds = list( filter(lambda num: num % 2, nums) )
# evens = list ( filter(lambda num: num % 2 == 0, nums) )
# print(odds)
# print(evens)

