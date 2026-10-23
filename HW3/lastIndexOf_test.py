import pytest

def lastIndexOf(numbers, num):
    """
        "numbers" - list with int numbers; "num" - int
        if "num" exists in "numbers", returns index of its last occurrence,
        otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
        lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    #TODO
    index = len(numbers) - 1
    while index >= 0:
        if numbers[index] == num:
            return index
        index -= 1
    return -1

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 3),
        ([10, 20, 30, 20, -1], 23, -1),
        ([5, 5, 5, 5], 5, 3),
        ([], 10, -1),
        ([3, 1, 2], 3, 0),
        ([1, 2, 3], 3, 2),
    ]
)
def test_last_index_of(numbers, num, expected):
    assert lastIndexOf(numbers, num) == expected
