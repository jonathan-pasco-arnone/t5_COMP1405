""" Binary search counter program """

# Created by: Jonathan Pasco-Arnone and Aidan Lalonde-Novales
# Created on: October 2023

import random
import time

def count(list, value):
    """ Determines the amount of times a value appears in a sorted list """
    # The +1 is to make sure both ends are inclusive
    return findend(list, value) - findstart(list, value) + 1

def findstart(list, value):
    """ Returns the index of the first occurrence of the value in the list """

    # Determines the starting top and bottom limits, as well as the range between them
    bottom_range = 0
    top_range = len(list) - 1
    full_range = top_range - bottom_range

    # Calculates the midpoint of the range (rounded down)
    index = int((top_range + bottom_range) / 2)

    # Continues until the range is between two numbers
    while full_range != 1:
        full_range = top_range - bottom_range

        # If the value is less than OR EQUAL to the middle of the list
        if value <= list[index]:
            top_range = index

        # If the value is greater than the middle of the list
        else:
            bottom_range = index

        # Calculates the midpoint of the range (rounded down)
        index = int((top_range + bottom_range) / 2)

    # Does the final check to figure out which of the final
    # two numbers is the first mention of the value
    if list[index] == value:
        return index
    else:
        return index + 1

def findend(list, value):
    """ Returns the index of the last occurrence of the value in the list """

    # Determines the starting top and bottom limits, as well as the range between them
    bottom_range = 0
    top_range = len(list) - 1
    full_range = top_range - bottom_range

    # Calculates the midpoint of the range (rounded down)
    index = int((top_range + bottom_range) / 2)

    # Continues until the range is between two numbers
    while full_range != 1:
        full_range = top_range - bottom_range

        # If the value is less thanthe middle of the list
        if value < list[index]:
            top_range = index

        # If the value is greater than OR EQUAL to the middle of the list
        else:
            bottom_range = index

        # Calculates the midpoint of the range (rounded down)
        index = int((top_range + bottom_range) / 2)

    # Does the final check to figure out which of the final
    # two numbers is the first mention of the value
    if list[index + 1] == value:
        return index + 1
    else:
        return index

values = []
# Generates the random list
for i in range(2500):
    values.append(random.randint(0,30000))
values.sort()

desired_numbers = []
# Generates the random numbers to check the count of in the list
for i in range(50000):
    desired_numbers.append(random.randint(0,30000))


start = time.time()
for number in desired_numbers:
    values.count(number)
end = time.time()
print("Linear time: ", (end-start))

start = time.time()
for number in desired_numbers:
    count(values, number)
end = time.time()
print("Hash time: ", (end-start))

# |-------Analysis-------|

# 1.
# The binary search count is SIGNIFICANTLY faster than the built in list count.

# 2.
# The longer the list the greater the distance between the two count methods in time. For example
# a list of 1 million items would take much more time for the linear count to complete. However a
# list of just 5 items is quicker for the linear count to complete.

# 3.
# Changing the range of the random numbers in the list does not seem to affect the runtime greatly.
# Having a range of 100,000 gave a similar result to a range of just 1.

# 4.
# Having a range of 30,000 for the numbers that will be counted and a range of 1 for the numbers
# that will be added to the list, gives a similar output to any other combination of these ranges.
# Therefore changing the range of the random numbers has at most a very minimal affect on the
# runtime of both counts.

# 5.
# Yes, these results makes sense because runtime complexity is primarily affected by size of the
# list inputted (Commonly represented as N). Furthermore, changing the amount of times the program
# runs with the "desired_numbers" input will not have a significant affect on the complexity
# because the binary count is unaffected by the quantity of desired numbers and the linear count
# can be affected both positively and negatively in an equal capacity.

# Linear count complexity = O(N)
# Binary count compexity = O(log N)
