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

# astr = 'Bob'
# try: 
#     print('Hello')
#     istr = int(astr) # won't work due to not a string with integers
#     print('There')
# except: 
#     istr = -1

# print('Done', istr) #would print "Hello", and "Done -1"

# x = 12
# if x == 12 :
#     print('Is 12')
#     print('Is Definitely 12')
#     print('Definitely 12')

# x = 0
# if x < 2:
#     print('Small')
# elif x < 10:
#     print('Medium')
# else:
#     print('Large')
# print('All Done')

# hrs = input('Enter Hours:')
# h = float(hrs)
# rate = input('Enter Rate:')
# r = float(rate)
# overtimeR = r * 1.5
# print(overtimeR)

# if h > 40:
#     # overtimeH are hours beyond 40 hours.
#     overtimeH = h - 40
#     print(overtimeH)
#     # hours beyond 40 hours should be paid at overtimeR 
#     overtime = overtimeH * overtimeR
#     print(overtime)
#     #bpay is basePay, should be hours (40) * 10.50 and equal 420
#     bpay = 40 * r
#     print(bpay)

#     gpay = bpay + overtime
#     print (gpay)
# else:
#     gpay = h * r
#     print(gpay)

# score = input("Enter Score Between 0.0 and 1.0:")
# sc = float(score)

# if sc >= 0.9:
#     print('A')
# elif sc >= 0.8:
#     print('B')
# elif sc >= 0.7:
#     print('C')
# elif sc >= 0.6:
#     print('D')
# elif sc < 0.6:
#     print('F')
# else:
#     print('Please Enter a Suitable Score')
#    

# hrs = input('Enter Hours:')
# h = float(hrs)
# rate = input('Enter Rate:')
# r = float(rate)
# overtimeR = r * 1.5
# print(overtimeR)

# if h > 40:
#     # overtimeH are hours beyond 40 hours.
#     overtimeH = h - 40
#     print(overtimeH)
#     # hours beyond 40 hours should be paid at overtimeR 
#     overtime = overtimeH * overtimeR
#     print(overtime)
#     #bpay is basePay, should be hours (40) * 10.50 and equal 420
#     bpay = 40 * r
#     print(bpay)

#     gpay = bpay + overtime
#     print (gpay)
# else:
#     gpay = h * r
#     print(gpay)

# def computepay(h, r):
#     if h > 40: 
#         overtime_hours = h - 40
#         overtime_pay = overtime_hours * overtime_rate
#         p = 40 * r + overtime_pay
#     else:
#         p = h * 10.50
#     return p

# hrs = input("Enter Hours:")
# h = float(hrs)

# rate = input("Enter Rate:")
# r = float(rate)
# overtime_rate = r * 1.5
# print(overtime_rate)

# p = computepay(h, r)
# print("Pay", p)

# tot = 0 
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
# print(tot)

# zork = 0
# for thing in [9, 41, 12, 3, 74, 15] :
#     zork = zork + thing
# print('After', zork)

# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)

# stuff = 'Hello World'
# type(stuff)

# print(dir(stuff))

# x = '40'
# y = int(x) + 2
# print(y)

# # Colors of the Rainbow
# colors_of_rainbow = ["red", "orange", "yellow", "green", "blue", "violet"]
# # print(type(colors_of_rainbow))
# # print(colors_of_rainbow)

# print(f'An acronym for the colors of the rainbow is ROYGBV, with the colors of the rainbow being  {colors_of_rainbow[0]}, {colors_of_rainbow[1]}, {colors_of_rainbow[2]}, {colors_of_rainbow[3]}, {colors_of_rainbow[4]}, and {colors_of_rainbow[5]}.')

# colors_of_rainbow[0] = "Macabre Red"
# colors_of_rainbow[1] = "Citrus Orange"
# colors_of_rainbow[2] = "Electric Yellow"
# colors_of_rainbow[3] = "Meadows Green"
# colors_of_rainbow[4] = "Sky Blue"
# colors_of_rainbow[5] = "Violent Violet"
# print(colors_of_rainbow)

# print(f'The new colors have been titled: {colors_of_rainbow[0]}, {colors_of_rainbow[1]}, {colors_of_rainbow[2]}, {colors_of_rainbow[3]}, {colors_of_rainbow[4]}, and {colors_of_rainbow[5]}.')

# # Job Applicants Lists
# .insert (1, "value")
# .pop() // last item in the list, .pop(0) will remove index[0]
# .append("value") // to the end of a list
# len()
# min() and max()
# sum()


# applicants = ["Kyndal", "Zach", "Charlie"]

# # Late application, add to end.
# applicants.append("Rob")
# print(applicants)

# # Kyndal is mispelled, change to Kendall
# index_kyndal = applicants.index("Kyndal")
# applicants[index_kyndal] = "Kendall"
# print(applicants)

# # Myles comes with recommendation, put him at the front of the list.
# applicants.insert(0, "Myles")
# print(applicants)

# # Where did Zach end up on the list's order?
# zach_pos = applicants.index("Zach")
# print(f'Zach is indexed at {zach_pos}, or position {zach_pos +1}.')

# # Charlie was accepted another offer, let's remove him from the list.
# applicants.remove("Charlie")
# print(applicants)

# # Your applicant at the front of the line was hired, remove him from the list.
# applicants.remove(applicants[0])
# print(applicants)

# # A new applicant did really well on his second interview from another department, let's put him second on the list.
# applicants.insert(1, "Christian")
# print(applicants)

# # Dictionary Practice
# apartment = {
#     "address": "123 Ocean Avenue",
#     "price": 100000,
#     "bedrooms": 3
# }

# # We need a tagline "Beautiful 3 bedroom apartment, priced at $100000."
# print(f"Beautiful {apartment['bedrooms']} bedroom apartment, priced at ${apartment['price']}.")

# # We need a zip code to put it up on StreetEasy.
# apartment["zip_code"] = "10011"
# print(apartment)

# # Landlord wants to sell it for more, increase the price by 20%.
# print(apartment["price"])
# apartment["price"] = int(apartment["price"] *1.20)
# print(apartment["price"])

# # We need to add square footage, let's say it's 2000sqft and price by square foot as well.
# apartment["square_foot"] = 2000
# print(apartment["square_foot"])

# apartment["price_per_sqft"] = round(apartment["price"] / apartment["square_foot"], 2) # round(dictionary["key"], //number of spaces to round//)
# print(apartment["price_per_sqft"])

# print(f'This apartment is {apartment["square_foot"]} square foot, and goes for ${apartment["price_per_sqft"]} per square foot.')
# print(apartment)

# # The apartment was sold, let's make note of it being sold and off the market.
# apartment["market_status"] = "sold"
# print(f'This aparment has been {apartment["market_status"]}!')
# print(apartment)

# n = 4
# if n % 2 == 0 and n > 20:
#     print("Not Weird")
# # if n is even and >2 and <5, print Not Weird
# elif n % 2 == 0 and 2 < n < 5:
#     print("Not Weird")
# # if n is even and >6 and <20, print Weird
# elif n % 2 == 0 and 6 < n < 20:
#     print("Weird")
# # if n is odd, print Weird
# else:
#     print("Weird")

# a = 5
# b = 2
# # sum of a + b
# sum = a + b

# # difference of a - b
# difference = a - b

# # product of a * b
# product = a * b

# print(sum)
# print(difference)
# print(product)

# a = 3
# b = 5
# integer_solution = int(a / b)
# print(integer_solution)
# float_solution = float(a / b)
# print(float_solution)

# For all non-negative integers i < n, print i^2.


# n = 10
# # while 1 <= n <= 20:
# #     print(n)
# #     print(n**2)
# #     n += 1

# for i in range(0, n):
#     print(i**2)

# year = 2000

# def is_leap(year):
#     # % 4 is a leap year unless % 100 unless ALSO % 400
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         leap = True
#     else:
#         leap = False
#     return leap

# # def is_leap(year):
# #     leap = False
# #     if 1900 <= year <= 10**5 and year % 4 == 0:
# #         leap = True
# #     else:
# #         leap = False
# #     return leap

# print(is_leap(year))

# # Print range of number in one line from 1 to n.
# n = 10
# for i in range (1, n + 1):
#     print(i, end="")
#     n += 1

#  #
# n = int(input())
# arr = map(int, input().split())
# # remove duplicate scores
# trimmed_scores = set(arr)

# # sort in reverse order and choose second place -- index[1]
# reverse_trimmed_scores = sorted(trimmed_scores, reverse=True)
# second_place = reverse_trimmed_scores[1]

# # print second place
# print(second_place)

# Python Librarian
authors = {
    "Frank Herbert": {
        "genre": "science fiction",
        "books": [
            "Dune",
            "Dune: Messiah"
        ],
        "active": True
    },
    "Lev Grossman": {
        "genre": "fantasy",
        "books": ["The Magicians 1", 
                  "The Magicians 2",
                  "The Magicians 3"
        ],
        "active": True
    }
}

# # Frank's First Book
# print(authors['Frank Herbert']['books'][0])

# # List all of the genres
# for author, details in authors.items():
#     print(details['genre'])

# genres = [details['genre'] for details in authors.values()]
# print(", ".join(genres))

# all_genres = []
# all_genres.append(authors["Frank Herbert"]["genre"])
# all_genres.append(authors["Lev Grossman"]["genre"])
# print(all_genres)

# # List All Books
# books = []
# # instead of books.append, use books.extend to merge books into a single list.
# books.extend(authors["Frank Herbert"]["books"])
# books.extend(authors["Lev Grossman"]["books"])
# # prints unified list/array of books.
# print(books)
# # prints with out being in brackets
# books_str = ", ".join(map(str, books))
# print(books_str)

# # Add "fiction" as a genre for Lev Grossman
# # option #1
# authors["Lev Grossman"]["genre"] = ["fantasy", "fiction"]
# # option #2 with append, after changing genre from a string to a list to be able to append
# authors["Lev Grossman"]["genre"] = [authors["Lev Grossman"]["genre"]]
# authors["Lev Grossman"]["genre"].append("fiction")

# print(authors["Lev Grossman"])

# # Delete an author The Magicians 3 //authors["authorvalue"]["second level books"]["index #"]
# del authors["Lev Grossman"]["books"][2]
# print(authors["Lev Grossman"])

price = 100

# if price < 10:
#     print(price * 1.10)
#     print("Is under 10")
# else:
#     print(price * 1.25)
#     print("Isn't under 10")

# customer = { "name": "Zachary Abercrombie", "status": "VIP" }
# if customer["status"] == "VIP":
#     price = price - (price * .20)
# print(price)

# bargain_bin = [
#     {"name": "90s Comedy DVD", "price": 2.99},
#     {"name": "80s Drama DVD", "price": 3.99}
# ]

# # conditional dictionary
# if bargain_bin[0]["price"] < bargain_bin[1]["price"]:
#     print(f'Your best value is the {bargain_bin[0]["name"]} for only ${bargain_bin[0]["price"]}.')
# else:
#     print(f'Your best value is the {bargain_bin[1]["name"]} for only ${bargain_bin[1]["price"]}.')

# letter = "a"
# if letter.lower() in {'a', 'e', 'i', 'o', 'u'}:
#     print(f'{letter} is a vowel.')
# else:
#     print(f'{letter} is not a vowel.')

# player = "rock"
# cpu = "scissors"

# if player == "rock":
#     if cpu == "scissors":
#         print(f'The Player wins with {player}!')
#     if cpu == "paper":
#         print(f'CPU wins with {cpu}!')

# if player == "paper":
#     if cpu == "rock":
#         print(f'The Player wins with {player}!')
#     if cpu == "scissors":
#         print(f'CPU wins with {cpu}!')

# if player == "scissors":
#     if cpu == "paper":
#         print(f'The Player wins with {player}!')
#     if cpu == "rock":
#         print(f'CPU wins with {cpu}!')

# a = 5
# b = 4
# c = 3

# if a == b == c:
#     print('Equalateral: All Sides are Equal')
# if a != b != c:
#     print('Scalene: All Sides are Unequal')
# if a == b != c or a == c != b or c == b != a:
#     print('Isosceles: Two Sides are the Same')

# Seasonal Challenge
# Dec 21 - Mar 19: Winter
# Mar 20 - Jun 20: Spring
# Jun 21 - Sep 21: Summer
# Sep 22 - Dec 20: Fall

# month = "December"
# day = 1

# # WINTER
# if month == "December" and 21 <= day <= 31 or month == "January" or month == "February" or month == "March" and 1 <= day <= 19:
#     print(f'{month} {day}, is in the Winter season.')
# # SPRING
# elif month == "March" and 20 <= day <= 31 or month == "April" or month == "May" or month == "June" and 1 <= day <= 20:
#     print(f'{month} {day}, is in the Spring Season.')
# # SUMMER
# elif month == "June" and 21 <= day <= 30 or month == "July" or month == "August" or month == "September" and 1 <= day <= 30:
#     print(f'{month} {day}, is in the Summer Season.')
# # FALL
# else: 
#     print(f'{month} {day}, is in the Fall Season.')

# boat = {
#     "has_fox": True,
#     "has_chicken": True,
#     "has_grain": False
# }

# # 1. If all three properties are true, print "The boat was too heavy and sank."
# if boat["has_chicken"] and boat["has_fox"] and boat["has_grain"]:
#     print('The boat has sank.')

# # 2. If the boat's has_fox and has_chicken properties are true, print "The fox ate the chicken.."
# if boat["has_fox"] and boat["has_chicken"] and not boat["has_grain"]:
#     print('The fox ate the chicken.')

# # 3. If the boat's has_chicken and has_grain propertes are true, print "The chicken ate the grain."
# if boat["has_chicken"] and boat["has_grain"] and not boat["has_fox"]:
#     print('The chicken ate the grain.')

# # 4. If none of them are in the boat, print "The boat is ready to use."
# if not (boat["has_chicken"] or boat["has_fox"] or boat["has_grain"]):
#     print('The boat is ready for use.')



