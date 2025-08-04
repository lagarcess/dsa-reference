import pytest
from .solution_01 import twoNumberSum as twoNumberSum_01
from .solution_02 import twoNumberSum as twoNumberSum_02
from .solution_03 import twoNumberSum as twoNumberSum_03

solutions_to_test = [
    twoNumberSum_01,
    twoNumberSum_02,
    twoNumberSum_03,
]

test_cases = [
        ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11]),
        ([4, 6, 1, -3], 3, [6, -3]),
        ([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5, [-5, 0]),
        #([15], 15, [15]), # TODO: debug this case
    ]

@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize(
    "nums, target, expected",
    test_cases
)
def test_two_number_sum(solution_func, nums, target, expected):
    result = solution_func(nums, target)
    assert sorted(result) == sorted(expected)
