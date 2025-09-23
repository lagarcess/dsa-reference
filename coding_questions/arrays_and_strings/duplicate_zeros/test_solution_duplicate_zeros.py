import pytest
from .solution_01 import duplicateZeros as duplicateZeros_01

solutions_to_test = [
    duplicateZeros_01,
]

test_cases = [
    ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
    ([1, 2, 3], [1, 2, 3]),
    ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]),
    ([8, 4, 5, 0, 0, 0, 0, 7], [8, 4, 5, 0, 0, 0, 0, 0]),
    ([1], [1]),
    ([0], [0]),
    ([1, 2, 3, 0], [1, 2, 3, 0]),
    ([1, 2, 3, 0, 4], [1, 2, 3, 0, 0]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 0, 2], [1, 0, 0]),
]


@pytest.mark.parametrize("solution", solutions_to_test)
@pytest.mark.parametrize("input_arr, expected", test_cases)
def test_duplicate_zeros(solution, input_arr, expected):
    failure_message = (
        f"Failed for input: {input_arr} with solution: {solution.__name__}"
    )
    assert solution(input_arr) == expected, failure_message
