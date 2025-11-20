import pytest
from .solution_01 import MinMaxStack as MinMaxStack_01
from .solution_02 import MinMaxStack as MinMaxStack_02
from .solution_03 import MinMaxStack as MinMaxStack_03

solutions_to_test = [
    MinMaxStack_01,
    MinMaxStack_02,
    MinMaxStack_03,
]

test_cases = [
    (
        [
            ("push", 5),
            ("push", 2),
            ("push", 8),
            ("getMin",),
            ("getMax",),
            ("pop",),
            ("getMin",),
            ("getMax",),
            ("pop",),
            ("getMin",),
            ("getMax",),
        ],
        [None, None, None, 2, 8, 8, 2, 5, 2, 5, 5],
    ),
    (
        [
            ("push", 1),
            ("push", 3),
            ("push", 0),
            ("getMin",),
            ("getMax",),
            ("pop",),
            ("getMin",),
            ("getMax",),
        ],
        [None, None, None, 0, 3, 0, 1, 3],
    ),
    (
        [
            ("push", 10),
            ("push", 20),
            ("push", 5),
            ("getMin",),
            ("getMax",),
            ("pop",),
            ("getMin",),
            ("getMax",),
            ("pop",),
            ("getMin",),
            ("getMax",),
        ],
        [None, None, None, 5, 20, 5, 10, 20, 20, 10, 10],
    ),
]


@pytest.mark.parametrize("solution_class", solutions_to_test)
@pytest.mark.parametrize("operations, expected", test_cases)
def test_min_max_stack(solution_class, operations, expected):
    stack = solution_class()
    results = []
    for operation in operations:
        method = operation[0]
        if method == "push":
            stack.push(operation[1])
            results.append(None)
        elif method == "pop":
            results.append(stack.pop())
        elif method == "getMin":
            results.append(stack.getMin())
        elif method == "getMax":
            results.append(stack.getMax())
    assert (
        results == expected
    ), f"Failed for operations: {operations} with solution: {solution_class.__name__}"
