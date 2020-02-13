from Week_5.Day_5.Anagram_Checker import AnagramChecker
from itertools import permutations

def initialize():
    checker = AnagramChecker()
    show_menu(checker)


def show_menu(anagram):
    while True:
        start = (input("Please Enter a Word or type 'X' to exit").upper())
        start = start.strip()
        if " " in start:
            print("You can only check one word at a time, please try again")
            continue
        elif not start.isalpha():
            print("That's not a valid word, please try again")
            continue
        elif start == "X":
            break
        else:
            print(f"Your word is {start}")
            print(f"The anagrams for {start} are {anagram.get_anagrams(start)}")
            print("This is a valid English word")

initialize()

