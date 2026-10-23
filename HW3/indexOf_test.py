import pytest

def indexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its first occurrence,
        otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
        indexOf([10, 20, 30, 20, -1],23) => -1
    """
    #TODO
    index = 0
    while index < len(numbers):
        if numbers[index] == num:
            return index
        index += 1
    return -1

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 1),
        ([10, 20, 30, 20, -1], 23, -1),
        ([5, 5, 5, 5], 5, 0),
        ([], 10, -1),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3], 1, 0),
    ]
)
def test_index_of(numbers, num, expected):
    assert indexOf(numbers, num) == expected
