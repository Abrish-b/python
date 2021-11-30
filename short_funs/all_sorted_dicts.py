
# ordered keys

def print_sorted_dictionary(a_dictionary):
    for ord_k in sorted(a_dictionary):
        print('{} : {}'.format(ord_k, a_dictionary[ord_k]))


a_dictionary = {'language': "C", 'Number': 89,
                'track': "Low level", 'ids': [1, 2, 3]}
print_sorted_dictionary(a_dictionary)

# add/replace a value


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

# del a key in dict


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


a_dictionary = {'language': "C", 'Number': 89,
                'track': "Low", 'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

# dict val mul by 2


def multiply_by_2(a_dictionary):
    mul_2 = dict()
    for k, v in a_dictionary.items():
        mul_2[k] = v*2
    return mul_2


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
