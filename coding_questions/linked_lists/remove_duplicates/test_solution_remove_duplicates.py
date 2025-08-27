import pytest
from linked_lists.single_linked_list import LinkedList
from .solution_01 import removeDuplicatesFromLinkedList as removeDuplicates_01
from .solution_02 import removeDuplicatesFromLinkedList as removeDuplicates_02

solutions_to_test = [
    removeDuplicates_01,
    removeDuplicates_02,
]

test_cases = [
    (LinkedList([1, 1, 3, 4, 4, 4, 5, 6, 6]), LinkedList([1, 3, 4, 5, 6])),
    (
        LinkedList([1, 2 - 1, 3 - 1, 2, 3, 5 - 2, 5 - 2, 4, 5, 7 - 2]),
        LinkedList([1, 2, 3, 4, 5]),
    ),
    (
        LinkedList([1, 2 - 1, 3 - 1, 4 - 1, 5 - 1, 6 - 1, 7 - 1]),
        LinkedList([1, 2, 3, 4, 5, 6]),
    ),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("linked_list, expected_output", test_cases)
def test_remove_duplicates(solution_func, linked_list, expected_output):
    result = solution_func(linked_list)
    actual = result.getNodesInArray()
    expected = expected_output.getNodesInArray()
    assert (
        actual == expected
    ), f"Expected {expected}, but got {actual} for {solution_func.__name__}"
