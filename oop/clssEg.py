#!/usr/bin/python3


# class person:

#     def __init__(self, Name, Age):
#         self.name = Name
#         self.age = Age

#     def say_hi(self):
#         print('Hello, my name is', self.name, 'and', self.age, 'old.')


# p1 = person("Abrham", 24)
# p2 = person("Ermias", 30)

# p1.say_hi()
# p2.say_hi()


class Square:
    def __init__(self, size):
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
