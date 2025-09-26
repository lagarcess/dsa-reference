import pytest  # type: ignore
from .solution_01 import moveElementToEnd as moveElementToEnd_01
from .solution_02 import moveElementToEnd as moveElementToEnd_02
from .solution_03 import moveElementToEnd as moveElementToEnd_03
from .solution_04 import moveElementToEnd as moveElementToEnd_04

solutions_to_test = [
    moveElementToEnd_01,
]
solutions_to_test_sorted = [
    moveElementToEnd_02,
    moveElementToEnd_03,
    moveElementToEnd_04,
]

test_cases = [
    # Regular case with multiple elements to move
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]),
    # Empty array
    ([], 3, []),
    # Array with no elements to move
    ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
    # Array with all elements being the target
    ([1, 1, 1, 1], 1, [1, 1, 1, 1]),
    # Single element array
    ([5], 5, [5]),
    # Two elements array (with target)
    ([2, 1], 2, [1, 2]),
    # Two elements array (without target)
    ([1, 2], 3, [1, 2]),
    # Target at start
    ([5, 1, 2, 3, 4], 5, [4, 1, 2, 3, 5]),
    # Target at end (already in position)
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    # Multiple targets scattered
    ([2, 4, 2, 5, 6, 2, 2], 2, [6, 4, 5, 2, 2, 2, 2]),
    # Array with alternating target elements
    ([2, 1, 2, 3, 2, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2]),
    # Large array with elements at extremes
    ([5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9], 5, [9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5]),
]


def get_expected_output_sorted(test_input, to_move):
    array = sorted(
        test_input, key=lambda x: x == to_move
    )  # Sort to maintain order for other solutions
    return array


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("test_input, to_move, expected", test_cases)
def test_move_element_to_end(solution_func, test_input, to_move, expected):
    result = solution_func(test_input, to_move)
    failed_message = f"""
    Failed for {solution_func.__name__} with input {test_input} and to_move {to_move},
    expected {expected} but got {result}"""
    assert result == expected, failed_message


@pytest.mark.parametrize("solution_func_sorted", solutions_to_test_sorted)
@pytest.mark.parametrize("test_input, to_move, expected", test_cases)
def test_move_element_to_end_sorted(
    solution_func_sorted, test_input, to_move, expected
):
    expected = get_expected_output_sorted(test_input, to_move)
    result = solution_func_sorted(test_input, to_move)
    failed_message = f"""
    Failed for {solution_func_sorted.__name__} with input {test_input} and to_move {to_move},
    expected {expected} but got {result}"""
    assert result == expected, failed_message
