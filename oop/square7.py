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
        if self.position >= (0, 0):
            for l in range(0, self.position[1]):
                sys.stdout.write('\n')
            for j in range(0, self.size):
                sys.stdout.write(
                    ''.join('_' for k in range(0, self.position[0])))
                sys.stdout.write(''.join('#' for l in range(0, self.size)))
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
        if value >= (0, 0) and type(value) is tuple:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
            return self.__size
