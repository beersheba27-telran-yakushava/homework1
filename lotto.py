import random

def exists(numbers, num):
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    #TODO
    return num in numbers

def distinct_random_numbers(min, max, size):
    """

    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    #TODO
    numbers = []

    while len(numbers) < size:
        num = random.randint(min, max)

        if exists(numbers, num):
            continue
        else:
            numbers.append(num)

    return numbers

print (distinct_random_numbers(1, 49, 7))
