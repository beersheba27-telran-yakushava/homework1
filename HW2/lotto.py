import random

def distinct_random_numbers(min, max, size):
    """
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    """
    #TODO
    if size > 0 and max - min + 1 >= size:
        return random.sample(range(min, max+1), size)

    return []

print (distinct_random_numbers(1, 49, 7))
