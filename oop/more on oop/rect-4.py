#!/usr/bin/python3


class Rectangle:
    """this defines a free class rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")

        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")

        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)

    def __str__(self):
        build = []
        if self.height == 0 or self.width == 0:
            build.append('')
        else:
            for i in range(self.height):
                build.append(''.join('#' for j in range(self.width)))
                build.append('\n')
        return "".join(build)


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))
