# unique Add
def uniq_add(my_list=[]):
    result = 0
    for i in set(my_list):
        result += i
    return result


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
