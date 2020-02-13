# Anagram Checker
from itertools import permutations
class AnagramChecker():

    def __init__(self):
        self.word_list = open("sowpods.txt", 'r').read()
        self.word_list = self.word_list.split("\n")

    def is_valid_word(self, word):
        if word in self.word_list:
            return True
        else:
            return False

    def get_anagrams(self, word):
        permlist = ["".join(items) for items in permutations(word)]
        anagrams = []
        for item in permlist:
            if self.is_valid_word(item):
                anagrams.append(item)
        return anagrams

    # def are_anagrams(self, word1, word2):


if __name__ == "__main__":

    checker = AnagramChecker()

    word = input("Please Enter a Word:").upper()
    anagrams = checker.get_anagrams(word)

    print(anagrams)