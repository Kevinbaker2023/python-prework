# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

hello_name("Kevin")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for value in range(1,101,2):
        print(value)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    print(max(a_list))

max_num_in_list([1, 2, 3, 4, 5])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        print(True)
    else:
        print(False)
    
is_leap_year(2023)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    if sorted(a_list) == list(range(min(a_list), max(a_list) + 1)):
        print(True)
    else:
        print(False)

is_consecutive([5, 4, 2, 1])