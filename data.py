######## Seyhan Van Khan
######## Data module
######## Generate list of numbers
######## January 2018

from random import choice, randint


def RandomList(num_numbers, min, max, inOrder=False):
    numbers = []
    while len(numbers) < num_numbers:
        numbers.append(randint(int(min), int(max)))
    return sorted(numbers) if inOrder else numbers
