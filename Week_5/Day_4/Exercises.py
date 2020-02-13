import random
class ForceWielder:

    def __init__(self, name):
        self.name = name
        self.power = random.randint(1, 16)
        self.wisdom = random.randint(1, 16)

    def train(self):
        pass

    def h_mean(self):
        power = self.power
        wisdom = self.wisdom
        return (power * wisdom) / (power + wisdom)

    def fight(self, another_jedi):
        if self.h_mean() > another_jedi.h_mean():
            print(f"{self.name} is the winner!")
        else:
            print(f"{another_jedi.name} has the high ground!")

    def is_jedi(self):
        pass

class Jedi(ForceWielder):
    def __init__(self, name, ls_color = "Green"):
        super().__init__(name)
        self.power = random.randint(1,16)
        self.wisdom = random.randint(1, 16 +10)
        self.lightsaber_color = ls_color

    def is_jedi(self):
        return True

    def find_ls_color(self):
        if self.power > self.wisdom:
            self.lightsaber_color = 'Blue'
            return "Blue"
        elif self.power == self.wisdom or self.name =="Mace Windu":
            return "Purple"
        else:
            return "Green"

    def train(self):
        wis = random.randint(10,21)
        pwr = random.randint(5,16)
        return self.wisdom + wis and self.power + pwr

class Sith(ForceWielder):
    def __init__(self, name, sith_name, ls_color ="Red"):
        super().__init__(name)
        self.power = random.randint(1, 16 + 10)
        self.wisdom = random.randint(1, 16)
        self.lightsaber_color = ls_color
        self.sith_name = sith_name

    def is_jedi(self):
        return False

    def train(self):
        wis = random.randint(5, 16)
        pwr = random.randint(10, 21)
        return self.wisdom + wis and self.power + pwr


the_senate = Sith("Sheev Palpatine","Darth Sidius")
the_count = Sith("Count Dooku", "Darth Tyrannus")
anakin = Sith("Anakin Skywalker","Darth Vader")

yoda = Jedi("Master Yoda")
obi_wan = Jedi("Obi-wan Kenobi")
mace = Jedi("Mace Windu")

# print(anakin.h_mean())
# anakin.fight(obi_wan)

# print(obi_wan.find_ls_color())

# obi_wan.train()
# anakin.train()
# print(anakin.fight(obi_wan))

# print(the_count.sith_name)
