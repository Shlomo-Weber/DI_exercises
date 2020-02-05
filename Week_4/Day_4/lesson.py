import random

# def talk():
#     p = random.random()
#     if p > 0.5:
#         return "whatever"
#     else:
#         print("coin toss")
#         return "something else"
#
# print(talk())

# def multiply(num, multiplier):
#     return num*multiplier
#
# print(multiply(10,5))
#
# mul =[multiply(2, multiplier) for multiplier in range(1,11)]
# print(mul)

# person = "shlomo"
# def say_name(person):
#     print(f"Hey {person}")
#
# say_name(person)

# args - can be used to tell the system that you're going to have many arguments, but you're not sure how many
# *args unpacks the list or objects, and puts them together, allows you to add more arguments than called in the function
# def show_names(*args):
#     for i, name in enumerate(args):
#         print(f"person number {i}: {name}")
#
# show_names('yair', 'shlomo', 'eran', 'mitch')


# kwargs - key word arguments

# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(key,value)
#
# # info = {'name': 'Fred', 'last name': 'herp', 'profession': 'worker'}
# #
# show_info(name = 'fred', last_name = 'herp', profession = 'worker')
#
# show_info()
# YEAR = 2020
# MONTH = 2
# DAY = 5
# def get_age(year: int, month: int, day: int):
#    if month >= MONTH:
#        age = YEAR - year
#    else:
#        age = YEAR - year - 1
#    return age
#
#
# def can_retire(sex, date_of_birth):
#     args = list(map(int, date_of_birth.split('/')))
#     month, day, year = args[0], args[1], args[2]
#     age = get_age(year, month, day)
#     print(f"Your age {age}")
#     if sex == "male":
#         return age >=67
#     else:
#         return age >=62
#
#
# print(can_retire("male", '1/5/1955'))