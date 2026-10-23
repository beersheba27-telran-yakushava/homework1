import pytest

def count(numbers, num) :
    """
        "numbers" - list with int numbers; "num" - int
        returns count of "num" occurrences in "numbers".
        Examples: count([10, 20, 30, 20, -1],20) => 2,
        count([10, 20, 30, 20, -1],23) => 0
    """
    #TODO
    counter = 0
    index = 0
    while index < len(numbers):
        if numbers[index] == num:
            counter += 1
        index += 1
    return counter

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 2),
        ([10, 20, 30, 20, -1], 23, 0),
        ([], 10, 0),
        ([5, 5, 5, 5, 5], 5, 5),
        ([1, 2, 3, 4, 1], 1, 2),
    ]
)
def test_count(numbers, num, expected):
    assert count(numbers, num) == expected
