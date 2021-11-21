#!/usr/bin/python3
import dis
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if lastDigit < 0:
    lastDigit = -(lastDigit)
con = str()
if lastDigit > 5:
    con = 'and is greater than 5'
elif lastDigit < 6 & lastDigit != 0:
    con = 'and is less than 6 and not 0'
else:
    con = 'and is 0'
print('Last digit of {} is {} {}'.format(number, lastDigit, con))

# ASCII 97- 122 lower case
# ASCII 65- 90 Upper case

for i in range(65, 91, 1):
    print('{}'.format(chr(i).lower()), end="|")

# except q and e

for k in range(97, 123, 1):
    if k == 113 or k == 101:
        pass
    else:
        print('{}'.format(chr(k)), end="")

# Decimals and Hex 0-98

for j in range(0, 99, 1):
    print('{} = {}'.format(j, hex(j)))


# Two Digit 0 - 100

for l in range(0, 100, 1):
    if l != 99:
        print('{:02}'.format(l), end=", ")
    else:
        print('{}'.format(l))


# lowest combo of 2 digits

for g in range(0, 10, 1):
    for h in range(0, 10, 1):
        if g != h and g < h and (g != 8 or h != 9):
            print('{}{}'.format(g, h), end=", ")
        elif g == 8 and h == 9:
            print('{}{}'.format(g, h))
        else:
            pass


def islower(c):
    if ord(c) in range(97, 123, 1):
        return True
    else:
        return False


print(islower('A'))


def uppercase(str):
    for i in str:
        up = ord(i)
        if up > 96 and up < 123:
            print(chr(up-32))
        else:
            print(chr(up))


uppercase('Best 98 lOck')


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return abs(number) % 10


print_last_digit(98)
print_last_digit(0)
print(print_last_digit(-1024))


def add(a, b):
    return a + b


print(add(1, 2))
print(add(98, 0))
print(add(100, -2))


def pow(a, b):
    return a**b


print('____________________')
print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

# fizz and buzz


def fizzbuzz():
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz', end=" ")
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz', end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end=" ")
        else:
            print(i, end=" ")


fizzbuzz()

# reverse Alphabet
# ASCII 97- 122 lower case d
# ASCII 65- 90 Upper case f

for d in range(122, 96, -2):
    print('{}{}'.format(chr(d), chr(d-1).upper()), end="")

print()

# remove function not C way


def remove_char_at(str, n):
    if abs(n) <= len(str):
        str = str.replace(str[n], '')
    return str


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))


# Byte Code

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a+b
    else:
        return a*b-c


dis.dis(magic_calculation)
