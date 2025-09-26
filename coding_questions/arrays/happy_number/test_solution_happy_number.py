import pytest  # type: ignore
from .solution_01 import isHappy as isHappy_01
from .solution_02 import isHappy as isHappy_02
from .solution_03 import isHappy as isHappy_03

solutions_to_test = [
    isHappy_01,
    isHappy_02,
    isHappy_03,
]
test_cases = [
    (19, True),
    (2, False),
    (1, True),
    (7, True),
    (4, False),
    (20, False),
    (100, True),
    (44, True),
    (85, False),
    (123, False),
    (999, False),
    (145, False),
    (86, True),
    (10, True),
    (37, False),
    (58, False),
    (89, False),
    (130, True),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("n, expected", test_cases)
def test_is_happy(solution_func, n, expected):
    failure_message = f"Failed for solution: {solution_func.__name__} with input n={n}"
    assert solution_func(n) == expected, failure_message
