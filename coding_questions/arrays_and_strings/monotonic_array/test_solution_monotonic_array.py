import pytest
from .solution_01 import isMonotonic as isMonotonic_01
from .solution_02 import isMonotonic as isMonotonic_02

solutions_to_test = [
    isMonotonic_01,
    isMonotonic_02,
]

test_cases = [
    # Strictly decreasing
    ([-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True),
    ([-1, -5, -10, -1100, -1101, -1102, -9001], True),
    # Strictly increasing
    ([1, 5, 10, 1100, 1101, 1102, 9001], True),
    ([1, 2, 3, 4, 5], True),
    # All elements equal
    ([7, 7, 7, 7], True),
    # Two elements
    ([1], True),
    ([2], True),
    ([1, 1], True),
    ([1, 2], True),
    ([2, 1], True),
    # Empty array
    ([], True),
    # Plateaus (repeated values in the middle)
    ([1, 2, 2, 3], True),
    ([3, 2, 2, 1], True),
    # Not monotonic (switches direction)
    ([1, 2, 1], False),
    ([3, 2, 3], False),
    ([1, 2, 2, 1], False),
    ([1, 1, 2, 1], False),
    # Negative, zero, positive
    ([-3, -2, -1, 0, 1, 2], True),
    ([2, 1, 0, -1, -2], True),
    ([0, 0, 0], True),
    # Large numbers and edge integer values
    ([2147483647, 2147483646, 0, -2147483648], True),
    ([-2147483648, 0, 2147483646, 2147483647], True),
    ([1, 2, 3, 2, 1], False),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("nums, expected", test_cases)
def test_is_monotonic(solution_func, nums, expected):
    failure_message = f"Failed for input: {nums} using {solution_func.__name__}"
    result = solution_func(nums)
    assert result == expected, failure_message
