import random
from Week_5.Day_4.Exercises import Jedi, Sith

the_senate = Sith("Sheev Palpatine", "Darth Sidius")
the_count = Sith("Count Dooku", "Darth Tyrannus")
anakin = Sith("Anakin Skywalker", "Darth Vader")

yoda = Jedi("Master Yoda")
obi_wan = Jedi("Obi-wan Kenobi")
mace = Jedi("Mace Windu")

the_sith = [the_senate, the_count, anakin]
the_jedi = [mace, yoda, obi_wan]

def jedi_battle(jedi, sith):
    if jedi.h_mean() > sith.h_mean():
        print(f"{jedi.name} has the high ground!")
        Jedi.train(jedi)
        the_sith.remove(sith)
    elif sith.h_mean() > jedi.h_mean():
        Jedi.train(jedi)
        print(f"{sith.sith_name} has destroyed you!")
        Sith.train(sith)

successes = 0
while the_sith:
    successes += 1
    if successes == 100:
        print("The Sith have conquered the galaxy")
        break
    jedi_battle(random.choice(the_jedi), random.choice(the_sith))
    if not the_sith:
        print("The Jedi have vanquished the Sith")
        break


