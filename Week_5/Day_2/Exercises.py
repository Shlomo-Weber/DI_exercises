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

    def deposit(self):
        amount = int(input("What bill do you want to deposit?"))
        if amount < 0:
            print("You cannot add a negative number")
        elif amount % 20 == 0 or amount % 50 == 0 or amount % 100 == 0:
           bills = int(input("How many bills?"))
           total = bills*amount + hapoalim.balance
           print(f"Deposit accepted! You deposited {bills*amount} shekels. Your current amount is {total} shekels")
           dep_agn = input("Do you want to make another deposit?")
           if dep_agn =="yes":
               self.deposit()
           elif dep_agn == "no":
              withd = input("Do you want to make a withdrawl?")
              if withd == "yes":
                  self.withdraw()
              elif withd == "no":
                  print("Thank you! Have a grand fucking day, you dog-faced pony soldier!")


        else:
            print("Must be a 20, 50 or 100")

# print("Deposit accepted, you now have " + str(amount + hapoalim.balance) + " shekels")
    def withdraw(self):
        amount = int(input("Please input an amount to withdraw"))
        if amount % 20 == 0 or amount % 50 == 0:
            print("Withdrawl accepted, your current balance is " + str(hapoalim.balance - amount) + " shekels")
        elif amount > hapoalim.balance:
            print("Withdrawl exceeds account limit")
        else:
            print("Not a valid entry, must be in increments of either 20 or 50 shekels")
            self.withdraw()



hapoalim = Account("shlomo", 500)

# hapoalim.withdraw(345)

class Owner(Account):
    def __init__(self, owner, balance, cc_num, password):
        super().__init__(owner, balance)
        self.cc_num = cc_num
        self.password = password
        self.attempts = 0


    def check_owner_info(self, cc_num, password):
        user_num = self.cc_num
        user_pass = self.password
        if cc_num == user_num and password == user_pass:
            print("Access granted")
            ask = input("What would you like to do?")
            if ask == "deposit":
                    self.deposit()
            if ask == "withdraw":
                    self.withdraw()
        elif self.attempts >= 2:
            print("You are locked out of this account")
        else:
            self.attempts +=1
            print(f"Your info is incorrect, {self.attempts}")



shlomo = Owner("shlomo", 500, 1234, "herpderp")

shlomo.check_owner_info(1234, "herpderp")
