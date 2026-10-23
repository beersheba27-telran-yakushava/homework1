import pytest

def min_even (numbers):
    """
        "numbers" - list with int numbers
        returns minimal even number
        assumption: at least one even number exists in "numbers"
        no need to check that assumption (usually the assumptions are never checked ) 
        example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    #TODO
    min_num = None
    index = 0
    
    while index < len(numbers):
        current = numbers[index]
        if current % 2 == 0:
            if min_num is None or current < min_num:
                min_num = current
        index += 1
        
    return min_num

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([-10001, 10, 20, 8, -7], 8),
        ([2, 4, 6, 8], 2),
        ([-2, -4, -6, -8], -8),
        ([1, 3, 5, 0, 7], 0),
        ([42], 42),
        ([10, -20, 30, -20], -20),
    ]
)
def test_min_even(numbers, expected):
    assert min_even(numbers) == expected
