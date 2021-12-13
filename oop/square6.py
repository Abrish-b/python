#!/usr/bin/python3
import sys

"""square with coordiantes
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size != 0 and self.position > (0, 0):
            for i, k in zip(range(0, self.size), range(0, self.position[0])):
                for j, m in zip(range(0, self.size), range(0, self.position[1])):
                    sys.stdout.write(k*'-')
                    sys.stdout.write(1*'#')
                sys.stdout.write('\n')
        else:
            sys.stdout.write('\n')

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and len(value) != 2 and value[0] is not int and value[0] < 0 and value[1] is not int and value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            set.__position = value

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
            return self.__size


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
