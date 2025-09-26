import pytest  # type: ignore
from .solution_01 import threeNumberSum as threeNumberSum_01
from .solution_02 import threeNumberSum as threeNumberSum_02
from .solution_03 import threeNumberSum as threeNumberSum_03

solutions_to_test = [
    threeNumberSum_01,
    threeNumberSum_02,
    threeNumberSum_03,
]

test_cases = [
    ([12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]),
    ([1, 2, 3], 6, [[1, 2, 3]]),
    ([1, 2, 3], 7, []),
    ([8, 10, -2, 49, 14], 57, [[-2, 10, 49]]),
    ([12, 3, 1, 2, -6, 5, 0, -8, -1], 0, [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]),
    (
        [12, 3, 1, 2, -6, 5, 0, -8, -1, 6],
        0,
        [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]],
    ),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5, []),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("array, targetSum, expected", test_cases)
def test_three_number_sum(solution_func, array, targetSum, expected):
    result = solution_func(array, targetSum)
    assert (
        result == expected
    ), f"Failed for {solution_func.__name__} with input {array} and targetSum {targetSum}. Expected {expected}, got {result}"
