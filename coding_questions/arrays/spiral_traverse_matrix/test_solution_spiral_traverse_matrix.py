import pytest
from .solution_01 import spiralTraverse as solution_01
from .solution_02 import spiralTraverse as solution_02
from .solution_03 import spiralTraverse as solution_03

solutions_to_test = [solution_01, solution_02, solution_03]
test_cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    (
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    ),
    ([[1]], [1]),
    ([[1], [2], [3], [4]], [1, 2, 3, 4]),
    ([[1, 2, 3, 4]], [1, 2, 3, 4]),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], [1, 2, 4, 6, 8, 7, 5, 3]),
    ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3]),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("test_input, expected", test_cases)
def test_spiral_traverse(solution_func, test_input, expected):
    failure_message = f"Failed for {solution_func.__name__} with input {test_input}, expected {expected}, but got {solution_func(test_input)}"
    assert solution_func(test_input) == expected, failure_message
