import pytest  # type: ignore
from .solution_01 import smallestDifference as smallestDifference_01
from .solution_02 import smallestDifference as smallestDifference_02
from .solution_03 import smallestDifference as smallestDifference_03
from .solution_04 import smallestDifference as smallestDifference_04


solutions_to_test = [
    smallestDifference_01,
    smallestDifference_02,
    smallestDifference_03,
    smallestDifference_04,
]

test_cases = [
    ([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17], [28, 26]),
    ([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17], [20, 17]),
    ([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031], [25, 1005]),
    (
        [10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
        [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530],
        [530, 530],
    ),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("arrayOne, arrayTwo, expected", test_cases)
def test_smallest_difference(solution_func, arrayOne, arrayTwo, expected):
    failed_message = f"Failed for {solution_func.__name__} with input {arrayOne} and {arrayTwo}. Expected {expected}, got {solution_func(arrayOne, arrayTwo)}"
    assert solution_func(arrayOne, arrayTwo) == expected, failed_message
