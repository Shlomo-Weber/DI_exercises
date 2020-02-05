# l = ["u", 4, [3,2,1], {"a":78}]
#
# for index in range(len(l)):
#     print(index, l[index])

# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#     elif i == 5:
#         print(i)
#         break

# While Loops

# i=0
# while i < 10:
#     print(i)
#     i +=1

# while True:
#     value = (input("input a number between 1 and 10"))
#
#     try:
#         value = int(value)
#     except ValueError:
#         print("not a number")
#         continue
#     # if not value.isdigit():
#     #     print("not a number")
#     #     continue
#
#     if 1 <= value <= 10:
#         print("thanks")
#         break
#     else:
#         print("not in the valid range, please try again")



# [num for num in range(10) if num%2 !=0]



# print({str(key):value for key,value in zip(range(5), range(5))})
#
# print(list(zip(range(5), range(5))))


#
# names = ["john", "eyal", "Michael"]
# ages = ["20", "35", "40"]
# print({name:age for name,age in zip(names,ages)})
#
# print(list(map(int, ages)))


# nums = []
# words = []
# all = ["herp", "derp", "lerp", 56, 74, 32]
# for i in all:
#     if type(i) == str:
#         words.append(i)
#     elif type(i) == int:
#         nums.append(i)
#


# print(words)
# print(nums)
# list = ["big", "bigger", "biggest"]
# print(sorted(list, key=len)[-1])

# Exercise XP
# Exercise 1
# a = 10
# b = 5
# if a > b:
#     print("hello world")

# Exercise 2
# import random
# inputs = []
# for i in range(3):
#     num = int(input("please input a number"))
#     inputs.append(num)
#
# # print(max(inputs))
# num1 = inputs[0]
# num2 = inputs[1]
# num3 = inputs[2]
# if num1 == num2 or num2 == num3 or num1==num3:
#     print(max(inputs))
# elif num1 > num2 and num1 > num3:
#     print(num1," is the greatest number")
# elif num2 >num1 and num2 >num3:
#     print(num2," is the greatest number")
# else:
#     print(num3," is the greatest number")

# Exercise 3
# 1. Make a list of months
# 2. ask the user for their month
# 3. make an if else statement that will return the user one of four seasons
# months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
# brthmonth = input("What month were you born in?")
# if brthmonth == months[4] or brthmonth == months[5] or brthmonth == months[6]:
#     print(f"Because you were born in {brthmonth}, you were also born in the Summer")
# elif brthmonth == months[1] or brthmonth == months[2] or brthmonth == months[3]:
#     print(f"Because you were born in {brthmonth}, you were also born in the Spring")
# elif brthmonth == months[10] or brthmonth == months[11] or brthmonth == months[0]:
#     print(f"Because you were born in {brthmonth}, you were also born in the Winter")
# elif brthmonth == months[7] or brthmonth == months[8] or brthmonth == months[9]:
#     print(f"Because you were born in {brthmonth}, you were also born in the Fall")
# else:
#     print("You are above time")

# Exercise 4
# Write a Python program to check whether an alphabet is a vowel or consonant.
# 1. Make a list of the entire alphabet
# 2. loop through it
# 3. make an if else statement for vowels
# 4. else, anything other than vowels is a consonant

# words=(input('write something'))
# for letters in words:
#     if letters == 'o' or letters=='a' or letters=='e' or letters=='i' or letters=='i':
#         print(f"{letters} is a vowel")
#     elif letters ==' ' or letters==',':
#         continue
#     else:
#         print(f"{letters} is a consonant")

# Exercise 5
# Write a Python program to guess a number between 1 to 9.
# 1. user input to guess a number
# 2. have the comp develop a random number
# 3. if the number is higher, say "your number is too low"
# 4. if too high, say "your number is too high"
# 5. you get 3 guesses
# 6. if you don't guess it, the comp says haha you suck, the number was ##
# import random
# compnum = random.randrange(1,10)
# for i in range(3):
#     mynum = int(input("Please choose a number between 1 and 10"))
#     if mynum == compnum:
#         print("You win you lucky sob")
#     elif mynum >compnum:
#         print("Your number is too big, try again")
#     elif mynum < compnum:
#         print("Your number is too low, try again")

# # Exercise 6
# l = range(1,21)
# for i in l:
#     print(i)

# Exercise 8
# nums = range(1,1000001)
# # print(min(nums))
# # print(max(nums))
# print(sum(nums))

# Exercise 9
# Draw the following pattern using for loops:
# space =" "
# for i in range(5):
#     space +="*"
#     print(space)

# Exercise 10
l = [1,2,3,4,5,6]
print(l.index(5))

# Exercise 11