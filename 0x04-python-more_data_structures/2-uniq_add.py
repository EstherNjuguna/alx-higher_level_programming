#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_unique = 0
    unique_elements = set()
    for i in my_list:
        if i not in unique_elements:
            unique_elements.add(i)
            sum_unique += i
    return sum_unique
