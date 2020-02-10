# class Animal:
# #     def __init__(self, l, c, h, n):
# #         self.legs = l
# #         self.color = c
# #         self.height = h
# #         self.name = n
# #         self.sleeping = False
# #
# #     def sleep(self):
# #         self.sleeping = True
# #         return f"{self.name} is sleeping"
# #     def eat(self):
# #         return f"{self.name} is eating"
# # a = Animal(4, "Brown", "3 meters", "Titan")
# #
# # print(a.sleeping)
# # print(a.sleep())
# # print(a.sleeping)
# #
# # class Dog(Animal):
# #     def bark(self):
# #         return f"{self.name} barks!"
# # dog = Dog(4, "red", "50 cm", "Sparky")
# #
# # class Shark(Animal):
# #     def sleep(self):
# #         return "Sharks don't sleep"
# #
# # shark = Shark(0, 'white', "50cm", "Elvis")
# # print(dog.sleep())
# # print(shark.sleep())

# Exercise 1
class Family():
    def __init__(self, last_name,):
        self.last_name = last_name
        self.members = []

    def addMember(self, name, age, sex, is_child):
        member_info = {
            "name":name,
            "age": age,
            "sex": sex,
            "is_child":is_child
        }
        self.members.append(member_info)

    def born(self, name, sex):
        print(f"{name} was born to the {self.last_name} family, they are a {sex}")
        self.addMember(name, 0, sex, True)

    def is_18(self, child):
        for children in self.members:
            if child in children.values():
                if children.get("age") >= 18:
                    print("You are over 18")
                else:
                    print("You aren't old enough")


    def __repr__(self):
        for members in self.members:
            print(members.get("name") + " is " + str(members.get("age")) + " years old, " )

myfam = Family("Weber")

myfam.addMember("Lisa", 63, 'Female', False)
myfam.addMember("Harold", 61, 'Male', False)
myfam.addMember("Ben", 34, "Male", True)
myfam.addMember("Ari", 33, "Male", True)
myfam.addMember("Penina", 30, "Female", True)
myfam.addMember("Chaim", 26, "Male", True)

# print(myfam.members)
# myfam.born("Shlomo","male")
# print(myfam.members)

# myfam.is_18("Chaim")

# myfam.__repr__()


# Exercise 2
class TheIncredibles(Family):
    def addMember(self, name, age, sex, is_child, power, incredible_name):
        member_info = {
            "name": name,
            "age": age,
            "sex": sex,
            "is_child": is_child,
            "power": power,
            "incredible_name":incredible_name
        }
        self.members.append(member_info)

    def use_power(self, incs):
        for member in self.members:
            if incs in member.values():
                if member.get("age") >= 18 and member.get("sex")=="Male":
                    print(f"{incs} uses his power")
                elif member.get("age") >= 18 and member.get("sex") == "Female":
                    print(f"{incs} uses her power")
                else:
                    print("You have no power here")
    def born(self, name, sex,):
        print(f"{name} was born to the {self.last_name} family, they are a {sex}")
        self.addMember(name, 0, sex, True, "Unknown power", "Jack-Jack" )

    def __repr__(self):
        for members in self.members:
            print(members.get("name") + " is " + str(members.get("age")) + " and is totally normal")

    def incredible_print(self):
        for members in self.members:
            print(members.get("incredible_name") + " is imbued with the power of " + members.get("power"))


    # def born(self, name, sex):
    #     print(f"{name} was born to the {self.last_name} family, they are a {sex}")
    #     self.addMember(name, 0, sex, True)

theincredibles = TheIncredibles("Parr")

theincredibles.addMember("Bob", 42, "Male", False, "Super Strength", "Mr. Incredible")
theincredibles.addMember("Helen", 39, "Female", False, "Elasticity", "Elastigirl")
theincredibles.addMember("Violet", 15, "Female", True, "Force Fields", "Violet")
theincredibles.addMember("Dashiell", 11, "Male", True, "Super Speed", "Dash")
# theincredibles.born("John","Male")
# print(theincredibles.members)

# theincredibles.use_power("Elastigirl")

# theincredibles.__repr__()
# theincredibles.incredible_print()


# Exercise 3
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("You cannot add a negative number")
        else:
            print("Deposit accepted, you now have " + str(amount + hapoalim.balance) + " shekels")
    # def withdraw(self):
hapoalim = Account("Shlomo", 500)

hapoalim.deposit(50)