#!/usr/bin/python3
def safe_print_division(my_list=[]):
    new = []
    for num in my_list:
        if num % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
