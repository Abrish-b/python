#!/usr/bin/python3
import string
import dis
from os import write
from calculator_1 import *
from variable_load_5 import a
import hidden_4 as hidden
import sys
from add_0 import add
from calculator_1 import add, sub, div, mul
a = 1
b = 2
print('{} + {} = {}'.format(a, b, add(a, b)))

a = 10
b = 5

print('{} + {} = {}'.format(a, b, add(a, b)))
print('{} - {} = {}'.format(a, b, sub(a, b)))
print('{} * {} = {}'.format(a, b, mul(a, b)))
print('{} / {} = {}'.format(a, b, div(a, b)))


if len(sys.argv) > 1:
    print('{} arguments:'.format(len(sys.argv)-1))
    for i in range(1, len(sys.argv)):
        print('{}: {}'.format(i, sys.argv[i]))
else:
    print('0 arguments.')
addis = 0
for l in range(1, len(sys.argv)):
    addis += int(sys.argv[l])

print(addis)

print(dir(hidden))


for i in dir(hidden):
    if i[:2] != '__':
        print(i)

print(a)


#Calculator

if len(sys.argv) == 4:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        print('{} {} {} = {}'.format(a, operator, b, add(a, b)))
        sys.exit(0)
    elif operator == '-':
        print('{} {} {} = {}'.format(a, operator, b, sub(a, b)))
        sys.exit(0)
    elif operator == '*':
        print('{} {} {} = {}'.format(a, operator, b, mul(a, b)))
        sys.exit(0)
    elif operator == '/':
        print('{} {} {} = {}'.format(a, operator, b, div(a, b)))
        sys.exit(0)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
else:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    sys.exit(1)

write(1, "#pythoniscool\n".encode("UTF-8"))


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


print(dis.dis(magic_calculation))

print(string.ascii_uppercase)
print(string.ascii_lowercase)
