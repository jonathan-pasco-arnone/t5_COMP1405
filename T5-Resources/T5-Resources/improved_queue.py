""" The improved queue program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: October 2023

def addend(list, dict, value):
    """ Adds a new value onto the end of the list and dictionary """
    list.append(value)

    # Creates a list for each key because each value could be put in multiple times
    # For example if the value 23 was at place 5 and 12 in the queue then the key 23
    # Would lead to the list [5,12]
    if dict.get(value) is None:
        dict[value] = [len(list) - 1] # The key is the value
    else:
        dict[value].append(len(list) - 1)

def removestart(list, dict):
    """ Pops the first value off of the list and dictionary """
    if len(list) == 0:
        return None

    # Move each value up one in the list
    for key in dict.keys():
        # For each value, there can be multiple locations in the queue
        # so we have to cycle through each one
        for duplicate_index in range(len(dict[key])):
            dict[key][duplicate_index] -= 1

    # Remove the first value of the list from the dictionary
    # Inside of the dictionary list of values, the 0th one will always be the first in line
    # Because of the previous for loop, the 0th value is now a -1
    dict[list[0]].remove(-1)
    # If the removed value makes the key empty, then remove the key
    if dict[list[0]] == []:
        del dict[list[0]]

    return list.pop(0)

def containslinear(list, value):
    """ Checks if the list contains a value """
    return value in list

def containshash(dict, value):
    """ Checks if a dictionary contains a value """
    if dict.get(value) is None:
        return False
    return True
