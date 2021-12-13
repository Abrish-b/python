import random
"""This is the squid Games Welcome
    the game is for the pure fun of
    evil mans pleasure
"""


class player:
    def __init__(self, number):
        self.number = number
        self.__will = random.randint(0, 9)
        self.love = random.randint(0, 9)
        self.__skill = random.randint(0, 9)
        self.knowlegde = random.randint(0, 9)


old_man = player(1)
print(old_man.__dict__)
