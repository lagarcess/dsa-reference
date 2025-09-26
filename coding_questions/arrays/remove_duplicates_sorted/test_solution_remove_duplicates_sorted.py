import pytest  # type: ignore
from .solution_01 import removeDuplicates as removeDuplicates_01
from .solution_02 import removeDuplicates as removeDuplicates_02

solutions_to_test = [removeDuplicates_01, removeDuplicates_02]

test_cases = [
    ([1, 1, 2], 2),
    ([2, 2, 2], 1),
    ([1, 2, 3], 3),
    ([], 0),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("input_list, expected_length", test_cases)
def test_remove_duplicates(solution_func, input_list, expected_length):
    nums = input_list.copy()
    new_length = solution_func(nums)
    assert new_length == expected_length
    assert nums[:new_length] == sorted(set(input_list))
