# number of keys in dict
def number_keys(a_dictionary):
    return len(list(a_dictionary))


a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
