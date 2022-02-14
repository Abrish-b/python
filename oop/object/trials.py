a = "banana"
b = "banana"

print(a == b)
print(a is b)
print(isinstance(str, object))

'''since strings are immutable they point to the same object that have the same value
    a --> "banana"
    b --> ^
'''
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print(list_a == list_b)
print(list_a is list_b)

'''but since lists are mutable they point to different objects
    list_a --> [1,2,3]
    list_b --> [1,2,3]
'''

# but in case aliasing the can point to the same object

list_1 = [1, 2, 3]
list_2 = list_1

# in this case list1 points to list2
for i, j in enumerate(list_1):
    print(i, j)
