# import math
import time
# class Writer:
#     def __init__(self, name, n_books, genre):
#         self.name = name
#         self.n_books = n_books
#         self.genre = genre
#     def write(self):
#         self.n_books +=1
#         print(f"{self.name} wrote a book")
#
#     @staticmethod
#     def say_hi():
#         print("hi!")
#
# if __name__ == '__main__':
#     albert=Writer(name="Albert Camus", n_books=25, genre=["Philosophy", "Roman"])
#     print(albert.name)
#     print(albert.n_books)
#     print(albert.genre)
#
# albert.write()
#
# albert.say_hi()
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius**2
#     @staticmethod
#     def compute_area(r):
#         return math.pi * r **2
#
# c = Circle(radius=2)
# # print(c.area())
# print(Circle.compute_area(r=5))
#
# class French:
#     def __init__(self,name):
#         self.name = name
#
#     def talk_nonsense(self):
#         print(f"{self.name} is talking: blah blah blah")
#
# class Philosopher(Writer):
#
#     def __init__(self, name, n_books, genre, domain):
#         super().__init__(name, n_books, genre)
#         self.domain = domain
#
#     def write_nonsense(self):
#         print(f"{self.name} writes {self.n_books} books about nonsense")
#
# herp = Philosopher("herpitus", 32, ["horror", "existetialism"], "lul")
# herp.write_nonsense()
#
# print(herp.domain)

# def decorator(func):
#     def wrapper():
#         print(f"running {func}")
#         func()
#         print("Done")
#     return wrapper
#
# @decorator
# def talk():
#     print("some words")
#
# talk()

def timeit(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter() - start
        print(f"function took {end} ")
    return wrapper

@timeit
def compute():
    return 2**6

compute()