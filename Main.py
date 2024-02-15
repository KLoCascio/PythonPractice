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

# # Python Lists/Loops/List Comprehension https://github.com/SEIR-0911/u4_lesson_python_lists_loops
# # Learn how to build and manipulate python lists
# # Learn how to loop through lists
# # Learn List Comprehension

# my_list = [1,2,3,4]
# other_list = list()

# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print('[0], index 0', days[0])
# print('[0:4], start at 0, and show four', days[0:4])
# print('[4:9], start at 4, and show 9, goes to Thursday, and shows Friday + 9, if value exists', days[4:9])
# print('[:4], everything upto and including the 4th', days[:4]) # everything upto and including the 4th
# print('[4:], everything after the fourth, but not including the 4th', days[4:]) # everything after the fourth, but not including the 4th
# print('[-4], fourth from the end', days[-4]) # fourth from the end

# nums = [1, 2, 3, 4, 5]
# chars = ['a', 'b', 'c', 'd', 'e']

# odds = [1, 3, 5, 7]
# evens = [2, 4, 6, 8]

# # Addition Operator
# all_nums = odds + evens
# print(all_nums)

# # Spread Operator
# spread_nums = [*odds, *evens]
# print(spread_nums)

# spread_nums.append(4)
# print(spread_nums)

# # Method	Description
# # .append( element )	Add a single element to the end of the list
# # .pop( index )	Removes element at the given index. If no index is specified, pop() removes and returns the last item in the list.
# # .index( element )	returns the index of the element in the list
# # .insert(index,element)	insert an element to the list at a specified index
# # .remove( element )	Removes the first item from the list equal to the input value
# # .count( element )	returns count of the element in the list
# # .reverse()	reverses the list
# # .sort()	sorts elements of a list
# # .copy()	returns a shallow copy of the list
# # len(list)	returns the total length of the list

# # LOOPS

# odds = [1, 3, 5, 7]
# evens = [2, 4, 6, 8]
# all_nums = odds + evens

# for num in all_nums[0:6]:
#     print(num)

# for num in range(0,10):
#     print(num)

# # # CHALLENGES # # #
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

# # LOOPS
# # The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

# if __name__ == '__main__':
#     n = int(input())
    
#     for i in range(n):
#         print(i ** 2)

# # # Leap Years
# # # In the Gregorian calendar, three conditions are used to identify leap years:
# # # The year can be evenly divided by 4, is a leap year, unless:
# # # The year can be evenly divided by 100, it is NOT a leap year, unless:
# # # The year is also evenly divisible by 400. Then it is a leap year.
# # # Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False. Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# def is_leap(year):
#     leap = False
    
#     # if year is divisible by 4 = true
#     if year % 4 == 0:
#         leap = True
    
#     # if year is evenly divisible by 100, it is not a leap year, unless it is also evenly divisible by 400
#     if year % 100 == 0:
#         leap = False
#         if year % 400 == 0:
#             leap = True
    
#     return leap

# year = int(input())
# print(is_leap(year))

# # PRINT FUNCTION
# # Without using any string methods, try to print the following: 1234...n. Note that "" represents the consecutive values in between.
# if __name__ == '__main__':
#     n = int(input())
    
#     for i in range(1, n + 1):
#         print(i, end="")

# # PYTHON FOR EVERYONE MICHIGAN U

# print("Good Morning!")

# # 2.3
# inp = input('Europe Floor? ')
# usf = int(inp) + 1
# print('US Floor', usf)

# print("123" + "abc")

# x = 1 + 2 * 3 - 8 / 4
# print(x)
# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")
# pay = float(hrs) * float(rate)
# print('Pay:', pay)



