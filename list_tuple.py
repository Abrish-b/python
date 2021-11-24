# integers of a list
# def print_list_integer(my_list=[]):
#     for i in range(0, len(my_list)):
#         print('{}'.format(my_list[i]))


# print_list_integer([1, 2, 3, 4, 5])
# def element_at(my_list, idx):
#     if idx > len(my_list)-1:
#         return None
#     elif idx < 0:
#         return None
#     else:
#         return my_list[idx]


# my_list = [1, 2, 3, 4, 5]
# idx = 5
# print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

# def print_reversed_list_integer(my_list=[]):
#     my_list.reverse()
#     for i in range(0, len(my_list)):
#         print('{}'.format(my_list[i]))


# my_list = [1, 2, 3, 4, 5]
# print_reversed_list_integer(my_list)

#
# def new_in_list(my_list, idx, element):
#     list_dup = my_list.copy()
#     if idx > len(my_list)-1:
#         return list_dup
#     elif idx < 0:
#         return list_dup
#     else:
#         list_dup[idx] = element
#         return list_dup


# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_element = 9
# new_list = new_in_list(my_list, idx, new_element)

# print(new_list)
# print(my_list)

# no C please
# def no_c(my_string):
#     if my_string.find('c') != -1 or my_string.find('C') != -1:
#         mystrDup = str()
#         for m in my_string:
#             if m == 'C' or m == 'c':
#                 pass
#             else:
#                 mystrDup += m
#         return mystrDup
#     else:
#         return my_string


# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# matrix = [[row[i] for row in matrix] for i in range(4)]

# print(matrix)

# print matrix
# def print_matrix_integer(matrix=[[]]):
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[i])):
#             print('{:d}'.format(matrix[i][j]), end=' ')
#         print()


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix)
# print("--")
# print_matrix_integer()


# def add_tuple(tuple_a=(), tuple_b=()):
#     new_tuple = tuple(())
#     a = list(tuple_a)
#     b = list(tuple_b)
#     sum_list = list()
#     do = False
#     if len(a) == len(b):
#         do = True
#     elif len(a) > len(b):
#         for i in range(len(b)-1, len(a)):
#             b.append(0)
#         do = True
#     else:
#         for i in range(len(a)-1, len(b)):
#             a.append(0)
#         do = True
#     if do == True:
#         for (item1, item2) in zip(a, b):
#             sum_list.append(item1+item2)
#             new_tuple = tuple(sum_list)
#     return new_tuple


# tuple_a = (1, 89)
# tuple_b = (88, 11)
# new_tuple = add_tuple(tuple_a, tuple_b)
# print(new_tuple)

# print(add_tuple(tuple_a, (1, )))
# print(add_tuple(tuple_a, ()))

# explanatory version

# def multiple_returns(sentence):
#     character = str()
#     size = 0
#     if len(sentence) == 0:
#         character = 'None'
#         size = 0
#     else:
#         character = sentence[0]
#         size = len(sentence)
#     ret = tuple((size, character))
#     return ret


# # shorter version


# def multiple_returns2(sentence):
#     if len(sentence) == 0:
#         return (0, None)
#     else:
#         return(len(sentence), sentence[0])


# sentence = "At school, I learnt C!"
# sentence2 = ""
# length, first = multiple_returns(sentence)
# length2, first2 = multiple_returns(sentence2)

# print("Length: {:d} - First character: {}".format(length, first))
# print("Length: {:d} - First character: {}".format(length2, first2))


# max of list

# def max_integer(my_list=[]):
#     max = 0
#     for i in range(0, len(my_list)):
#         if my_list[i] > max:
#             max = my_list[i]
#     return max


# my_list = [1, 90, 2, 13, 34, 5, -13, 3]
# max_value = max_integer(my_list)
# print("Max: {}".format(max_value))


# multiple of 2 in list
# def divisible_by_2(my_list=[]):
#     div = list()
#     for i in range(0, len(my_list)):
#         if my_list[i] % 2 == 0:
#             div.append(True)
#         else:
#             div.append(False)
#     return div


# my_list = [0, 1, 2, 3, 4, 5, 6]
# list_result = divisible_by_2(my_list)

# i = 0
# while i < len(list_result):
#     print("{:d} {:s} divisible by 2".format(
#         my_list[i], "is" if list_result[i] else "is not"))
#     i += 1

# delete at an index in a list

# def delete_at(my_list=[], idx=0):
#     if idx < 0 or idx > len(my_list):
#         return my_list
#     else:
#         my_list.remove(my_list[idx])
#         return my_list


# my_list = [1, 2, 3, 4, 5]
# idx = 3
# new_list = delete_at(my_list, idx)
# print(new_list)
# print(my_list)

# switcher

#!/usr/bin/python3
# a = 89
# b = 10
# a, b = b, a
# print("a={:d} - b={:d}".format(a, b))
