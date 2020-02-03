# selection_menu = None
#
# menu_text = 'Welcome to the menu\n _______\n please choose what youd like to do:\na. print hello\nb. say your name\nx. exit'
# while selection_menu !='x':
#     selection_menu = input(menu_text)
#     if selection_menu == 'a':
#         print('hello')
#     elif selection_menu == 'b':
#         user_name = input('tell me your name')
#         print(f'\nHello {user_name}\n')

# Exercise 2
# my_fav_numbers = {10,613,7,13}
# print(my_fav_numbers)
#
# my_fav_numbers.add(45)
# print(my_fav_numbers)
# my_fav_numbers.add(36)
# print(my_fav_numbers)
# my_fav_numbers.remove(13)
# print(my_fav_numbers)
#
# friend_favorite_nums = {23, 4, 7}
# our_fav_nums = friend_favorite_nums.union(my_fav_numbers)
# print(our_fav_nums)

# Exercise 3
# my_nums = (2,3,4,5)
# fnums = (6,7,8)
# ournums = my_nums + fnums
# print(ournums)

# Exercise 4
# list= []
# a = range(2)
# for n in a:
#     if n == 2:
#         list.append(n)
#     else:
#         list.append(-1n*2)
# print(list)

# Ninja Exercise
import sys
import random

user_string = input("please write something more than 10 letters")
if len(user_string) != 10:
    sys.exit(1)
    print(user_string)

info = f"First Character: {user_string[0]}, Last Character: {user_string[-1]}"
print(info)

for i in range(1, len(user_string)+1):
    print(user_string[:i])

# jumbled = copy(user_string)
# jumbled = random.shuffle(list(jumbled))
# jumbled = "".join(jumbled)
#
# print("jumbled string: {}".format(jumbled))