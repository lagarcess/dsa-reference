import pytest
from .solution_01 import moveElementToEnd as moveElementToEnd_01
from .solution_02 import moveElementToEnd as moveElementToEnd_02
from .solution_03 import moveElementToEnd as moveElementToEnd_03

solutions_to_test = [
    moveElementToEnd_01,
    moveElementToEnd_02,
    moveElementToEnd_03,
]

test_cases = [
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]),
    ([], 3, []),
    ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
    ([1, 1, 1, 1], 1, [1, 1, 1, 1]),
    ([3, 1, 2, 4, 5], 5, [3, 1, 2, 4, 5]),
    ([1, 2, 4, 5, 3], 3, [1, 2, 4, 5, 3]),
    ([2, 4, 2, 5, 6, 2, 2], 2, [6, 4, 5, 2, 2, 2, 2]),
    (
        [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12],
        5,
        [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5],
    ),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("test_input, to_move, expected", test_cases)
def test_move_element_to_end(solution_func, test_input, to_move, expected):
    failed_message = f"Failed for {solution_func.__name__} with input {test_input} and to_move {to_move}"
    assert solution_func(test_input, to_move) == expected, failed_message
