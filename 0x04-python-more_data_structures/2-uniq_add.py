#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    added_set = set(my_list)
    for i in added_set:
        result += i
    return result
