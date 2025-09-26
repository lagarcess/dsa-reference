import pytest  # type: ignore
from .solution_01 import longestPeak as solution_01

solutions_to_test = [solution_01]
test_cases = [
    ([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], 6),
    ([1, 3, 2], 3),
    ([1, 2, 3, 4, 5, 1], 6),
    ([1, 2, 3, 2, 1], 5),
    ([5, 4, 3, 2, 1], 0),
    ([1, 2, 3, 4, 5], 0),
    ([1], 0),
    ([1, 2], 0),
    ([2, 1], 0),
    ([1, 2, 1], 3),
    ([1, 2, 3, 4, 5, 4, 3, 2, 1], 9),
    ([0, -1, -2, -3, -4], 0),
    ([-4, -3, -2, -1, 0], 0),
    ([-2, -1, -2], 3),
    ([-10, -5, -1, -5, -10], 5),
    ([1, 2, 3, 4, -10, -5, -1], 5),
    (
        [
            1,
            1,
            1,
            2,
            3,
            10,
            12,
            -3,
            -3,
            2,
            3,
            45,
            800,
            99,
            98,
            0,
            -1,
            -1,
            2,
            3,
            4,
            5,
            0,
            -1,
            -1,
        ],
        9,
    ),
]


@pytest.mark.parametrize("solution", solutions_to_test)
@pytest.mark.parametrize("array, expected", test_cases)
def test_longest_peak(solution, array, expected):
    failure_message = f"Failed for solution: {solution.__name__} with input array: {array}, got {solution(array)}, expected {expected}"
    assert solution(array) == expected, failure_message
