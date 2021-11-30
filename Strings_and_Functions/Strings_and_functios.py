#!/usr/bin/python3
number = 3.14159
strVar = "Holberton School"
name1 = str()

print('FLoat: {:.2f}'.format(number))
print(3*strVar)
print('{:.10}'.format(strVar))
print(name1)
print(id(name1))
print("A's ASCII: {}".format(ord('A')))
print('ASCII code 65 represent character: {}'.format(chr(65)))

"""
len()	returns length of the string
max()	returns character having highest ASCII value
min()	returns character having lowest ASCII value
"""

s1 = "Welcome"

print("come" in s1)

print("come" not in s1)

print("tim" == "tie")

print("free" != "freedom")

print("arrow" > "aron")

print("right" >= "left")

print("teeth" < "tee")

print("yellow" <= "fellow")

print("abc" > "")

s = "hello"
for i in s:
    print(i, end="")
    """
    By default, print() function prints string with a newline, we change this behavior by passing named keyword argument called end as follows.
    """


"""
isalnum()	Returns True if string is alphanumeric
isalpha()	Returns True if string contains only alphabets
isdigit()	Returns True if string contains only digits
isidentifier()	Return True is string is valid identifier
islower()	Returns True if string is in lowercase
isupper()	Returns True if string is in uppercase
isspace()	Returns True if string contains only whitespace
"""
s = "welcome to python"

print(s.isalnum())
print("Welcome".isalpha())
print("2012".isdigit())
print("first Number".isidentifier())
print(s.islower())
print("WELCOME".isupper())
print("  \t".isspace())

"""
endswith(s1: str): 
        bool	Returns True if strings ends with substring s1
startswith(s1: str): 
        bool	Returns True if strings starts with substring s1
count(substring): 
        int	Returns number of occurrences of substring the string
find(s1): 
        int	Returns lowest index from where s1 starts in the string, if string not found returns -1
rfind(s1): 
        int	Returns highest index from where s1 starts in the string, if string not found returns -1
"""

#s = "welcome to python"

print(s.endswith("thon"))

print(s.startswith("good"))

print(s.find("come"))

print(s.find("become"))

print(s.rfind("o"))

print(s.count("o"))

"""
capitalize(): 
        str	Returns a copy of this string with only the first character capitalized.
lower(): 
        str	Return string by converting every character to lowercase
upper(): 
        str	Return string by converting every character to uppercase
title():
        str	This function return string by capitalizing first letter of every word in the string
swapcase(): 
        str	Return a string in which the lowercase letter is converted to uppercase and uppercase to lowercase
replace(old\, new): 
        str	This function returns new string by replacing the occurrence of old string with new string
"""

s = "string in python"

s1 = s.capitalize()
print(s1)

s2 = s.title()
print(s2)

s = "This Is Test"
s3 = s.lower()

print(s3)

s4 = s.upper()
print(s4)

s5 = s.swapcase()
print(s5)

s6 = s.replace("Is", "Was")
print(s6)

print(s)
