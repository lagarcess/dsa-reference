import pytest
from .solution_01 import twoSumIndex as twoSumIndex_01

solutions_to_test = [
    twoSumIndex_01,
]

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize(
    "nums, target, expected",
    test_cases
)
def test_two_sum_index(solution_func, nums, target, expected):
    result = solution_func(nums, target)
    assert result == expected
