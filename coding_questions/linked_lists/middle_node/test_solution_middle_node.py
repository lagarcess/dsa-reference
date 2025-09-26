import pytest  # type: ignore
from linked_lists.single_linked_list import LinkedList
from .solution_01 import middleNode as middleNode_01
from .solution_02 import middleNode as middleNode_02
from .solution_03 import middleNode as middleNode_03

solutions_to_test = [
    middleNode_01,
    middleNode_02,
    middleNode_03,
]

test_cases = [
    # Assuming LinkedList is a class that takes a list of values to create a linked list
    (LinkedList([1]), 1),
    (LinkedList([2, 3]), 3),
    (LinkedList([5, 7, 6, 9]), 6),
    (LinkedList([1, 2, 3, 4, 5]), 3),
    (LinkedList([1, 2, 1 - 2, 4, 5, 5 - 2, 10]), 4),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("linked_list, expected_middle", test_cases)
def test_middle_node(solution_func, linked_list, expected_middle):
    result = solution_func(linked_list)
    assert result.value == expected_middle
