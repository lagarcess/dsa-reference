import pytest  # type: ignore
from .solution_01 import reverseStr as reverseStr_01
from .solution_02 import reverseStr as reverseStr_02
from .solution_03 import reverseStr as reverseStr_03

solutions_to_test = [
    reverseStr_01,
    reverseStr_02,
    reverseStr_03,
]
test_cases = [
    # Basic 2k block cases
    ("abcdefg", 2, "bacdfeg"),
    ("abcdef", 2, "bacdfe"),
    # Edge cases - minimum length
    ("a", 2, "a"),
    ("ab", 2, "ba"),
    ("abc", 2, "bac"),
    # Various k values
    ("abcdef", 3, "cbadef"),
    ("abcdefg", 3, "cbadefg"),
    # Less than k remaining
    ("abcde", 2, "bacde"),
    ("abcdefgh", 3, "cbadefhg"),
    # k larger than string
    ("abcd", 5, "dcba"),
    ("abcdef", 7, "fedcba"),
    # Multiple 2k blocks
    ("abcdefghijkl", 2, "bacdfeghjikl"),
    # Different k sizes
    ("abcdefghijkl", 3, "cbadefihgjkl"),
    ("abcdefghijkl", 4, "dcbaefghlkji"),
    # Pattern consistency
    ("abcdefghijklmnop", 2, "bacdfeghjiklnmop"),
    # Repeated characters
    ("aaabbbcccddd", 3, "aaabbbcccddd"),
    # Longer string case
    ("abcdefghijklmnopqrst", 3, "cbadefihgjklonmpqrts"),
]


@pytest.mark.parametrize("solution_func", solutions_to_test)
@pytest.mark.parametrize("s, k, expected", test_cases)
def test_reverseStr(solution_func, s, k, expected):
    failure_message = (
        f"Failed for solution: {solution_func.__name__} with input s='{s}' and k={k}"
    )
    assert solution_func(s, k) == expected, failure_message
