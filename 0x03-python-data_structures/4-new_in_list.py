#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None
    new_made = my_list.copy()
    new_made[idx] = element
    return new_made
