# technical interview
# roman to integer

def roman_to_int(roman_string):
    num = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or None:
        return 0
    else:
        for i in range(0, len(roman_string)):
            if roman_string[i] in roman_dict:
                if (i+1) <= (len(roman_string)-1) and roman_dict[roman_string[i]] < roman_dict[roman_string[i+1]]:
                    num -= roman_dict[roman_string[i]]
                else:
                    num += roman_dict[roman_string[i]]
            else:
                num += 0
        return num


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
