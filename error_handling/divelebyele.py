# # liitle broken

# def list_division(my_list_1, my_list_2, list_length):
#     new_list = [None] * (list_length-1)
#     for ad in range(len(my_list_1), list_length):
#         my_list_1.append(None)
#     for ad in range(len(my_list_2), list_length):
#         my_list_2.append(None)
#     for x, y, z in zip(my_list_1, my_list_2, range(0, list_length)):
#         try:
#             print(z)
#             new_list.insert(z, x/y)
#             print(new_list)
#         except ZeroDivisionError:
#             print("division by 0")
#             new_list[z] = 0
#             print(new_list)
#         except TypeError:
#             print("wrong type or out of range")
#             new_list[z] = 0
#             print(new_list)
#     return new_list

# better way
def list_division(my_list_1, my_list_2, list_length):
    newList = list()
    for elem in range(0, list_length):
        try:
            newList.append(my_list_1[elem]/my_list_2[elem])
        except TypeError:
            print("wrong type")
            newList.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)

    return newList


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
