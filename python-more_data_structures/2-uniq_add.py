#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set(my_list)
    total = 0

    for i in unique_values:
        total += i

    return total
