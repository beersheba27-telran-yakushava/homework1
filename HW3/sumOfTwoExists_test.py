import pytest

def sumOfTwoExists(numbers, sum):
    """
        Optional task for advanced students
        To apply only the types discussed at the course up to now
        "numbers" - list with int numbers; "sum" - int
        returns True if "numbers" includes two numbers, sum of which equals "sum"
        Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
        sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    #TODO
    i = 0
    length = len(numbers)
    
    while i < length:
        j = i + 1
        while j < length:
            if numbers[i] + numbers[j] == sum:
                return True
            j += 1
        i += 1
        
    return False

@pytest.mark.parametrize(
    "numbers, sum, expected",
    [
        ([1, -1, 40, 50, 0], 0, True),
        ([1, -1, 40, 50, 0], 42, False),
        ([10, 20, 30], 40, True),
        ([5, 10, 15], 10, False),
        ([5, 5, 15], 10, True),
        ([1, 2], 3, True),
        ([1], 1, False),
        ([], 0, False),
    ]
)
def test_sum_of_two_exists(numbers, sum, expected):
    assert sumOfTwoExists(numbers, sum) == expected
