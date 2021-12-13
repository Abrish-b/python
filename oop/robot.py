#!/usr/bin/python3
import random


class Robot:
    """this is a robot class"""

    population = 0

    def __init__(self, name):
        """my name is ..yuh"""
        self.name = name
        self.__skill = random.randint(0, 9)
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    def getSkill(self):
        print("skill of {} out of 9: {}".format(self.name, self.__skill))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid1.getSkill()


droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

droid2.getSkill()

print(Robot.__init__.__doc__)
print(Robot.__dict__)
droid1.die()
droid2.__class__.how_many()
