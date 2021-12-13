#!/usr/bin/python3


"""Square with print # -> stdout
"""
import sys


class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size != 0:
            for i in range(0, self.size):
                for j in range(0, self.size):
                    sys.stdout.write('#')
                sys.stdout.write('\n')
        else:
            sys.stdout.write('\n')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
            return self.__size


my_square = Square(3)
print(Square.__str__)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
