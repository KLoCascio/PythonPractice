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

# # INTRO
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

# for i in range(10):
#     print (i//3, i%3)

a = 10
b = 6

print(a//b, a%b)