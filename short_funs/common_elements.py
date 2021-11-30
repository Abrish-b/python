
# print common elements of a list
# longer version
def common_elements(set_1, set_2):
    result = list()
    for x in set_1:
        for y in set_2:
            if y == x:
                result.append(x)
    return result
# shorter version


def common_elements2(set_1, set_2):
    return (set_1 & set_2)


set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements2(set_1, set_2)
print(sorted(list(c_set)))
