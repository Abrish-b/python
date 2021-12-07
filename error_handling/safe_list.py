def safe_print_list(my_list=[], x=0):
    try:
        for elem in range(0, x):
            print(my_list[elem], end="")
    except IndexError:
        count = 0
        for elem in my_list:
            count += 1
        return count
    else:
        return x
    finally:
        print(end="\n")


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
