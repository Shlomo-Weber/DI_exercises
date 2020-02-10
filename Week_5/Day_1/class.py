# class House:
#     def __init__(self, city, num_rooms, landlord):
#         self.city = city
#         self.num_rooms = num_rooms
#         self.landlord = landlord
#
#         self.rent = 1000 * self.num_rooms
#         if city == "TA":
#             self.rent *=2
#
#         def sign_contract(self, name, date):
#             if self.landlord == "Moti":
#                 self.rent *=2
#
#             print(f"Rental agreement between {name} and {self.landlord}")
#
#         def complain_about_broken_window(self):
#             print(f"{self.landlord} says: sorry i cant help")

# Exercise 1
# class Dog:
#
#     def __init__(self, dogName, dogHeight):
#         self.dogName = dogName
#         self.dogHeight = dogHeight
#
#     def talk(self):
#         print(f"woof, My name is {self.dogName}")
#
#     def jump(self, height):
#         print(self.dogHeight * 2)
#
#
# davids_dog = Dog("Rex", 50)
# sarahs_dog = Dog("Teacup", 20)
# # davids_dog.jump(50)
# # sarahs_dog.talk()
#
# def check_height():
#     if davids_dog.dogHeight > sarahs_dog.dogHeight:
#         print(f"{davids_dog.dogName} is the winner")
#     else:
#         print(f"{sarahs_dog.dogName} is the winner")
#
# check_height()

# Exercise 2
class Zoo:
    def __init__(self, zooName):
        self.zooName = zooName
        self.animals = list()

    def addAnimal(self, newAnimal):
        if newAnimal not in self.animals:
            self.animals.append(newAnimal)
        else:
            print("That animal is already in the zoo")

    def getAnimals(self):
        print(self.animals)

    def sellAnimal(self, animal_to_remove):
        self.animals.remove(animal_to_remove)
        print(f"Goodbye {animal_to_remove}")

    def sortAnimal(self, animals):
        sorted_animals = self.animals.sort()
        print(sorted_animals)
        temp = 0
        pen = {}
        for x,y in zip(animals[::], animals[1::]):
            if x[0] == y[0]:
                pen[temp] = [x,y]
            else:
                temp +=1
                pen[temp] = (x)
                pen[temp] = (y)
        print(pen)

bronx_zoo = Zoo("Bronx Zoo")

bronx_zoo.addAnimal("zebra")
bronx_zoo.addAnimal("gorilla")
bronx_zoo.addAnimal("lion")
bronx_zoo.addAnimal("tiger")
bronx_zoo.addAnimal("t-rex")
# bronx_zoo.getAnimals()
bronx_zoo.sortAnimal()

class Integer:
    def __init__(self, num_list):
        self.num_list = num_list

        def findlist(self):
            while 


my_list = Integer([4,5,6])