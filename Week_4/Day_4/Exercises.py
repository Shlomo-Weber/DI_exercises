import random

# temp = random.randint(-10, 41)
# Exercise XP 1

# season = input("what season is it")
# def get_random_temp(blah):
#     if blah == "winter":
#         return random.randint(-10, 17)
#     elif blah == "autumn" or blah == "fall":
#         return random.randint(17, 24)
#     elif blah == "spring":
#         return random.randint(24, 30)
#     elif blah == "summer":
#         return random.randint(30, 41)
#
#
# def main():
#     temperature = get_random_temp(season)
#     print(f"The temperature right now is {temperature} Celcius")
#     if season == "winter":
#         print("It's freezing outside")
#     elif season == "autumn" or season == "fall":
#         print("It's pretty chilly out there, don't forget your coat")
#     elif season == "spring":
#         print("it's pretty comfy outside")
#     else:
#         print("It's hot af, remember to hydrate")

# main()

#
# Exercise 2

def throw_dice():
    roll = random.randrange(1,7)
    return roll
# print(throw_dice())
def throw_until_doubles():
    first = throw_dice()
    second = throw_dice()
    count = 1
    while first != second:
        count += 1
        first = throw_dice()
        second = throw_dice()
    return count

# print(throw_until_doubles())

count_list = []
def main():
    for throws in range(100):
        doubles = throw_until_doubles()
        count_list.append(doubles)
    print(count_list)
    sum_of_throws =  sum(count_list)
    print(f"It took {sum_of_throws} to reach 100 doubles")
    print(sum_of_throws/100, " is the average")

main()