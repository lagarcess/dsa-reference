# Min Max Construction

## Problem Statement

Write a `MinMaxStack` class for a Min Max Stack. The class should support:
- Pushing and popping values on and off the stack.
- Peeking at the top value of the stack.
- Getting both the minimum and maximum values in the stack at any given time.

All class methods, when considered independently, should run in constant time and with constant space.

## Sample Usage
```python
min_max_stack = MinMaxStack()
min_max_stack.push(5)
min_max_stack.push(7)
min_max_stack.push(2)
print(min_max_stack.get_min())  # Output: 2
print(min_max_stack.get_max())  # Output: 7
min_max_stack.pop()
print(min_max_stack.peek())      # Output: 7
print(min_max_stack.get_min())  # Output: 5
print(min_max_stack.get_max())  # Output: 7
```

## Hints
1. **Auxiliary Stacks**: Consider using two additional stacks to keep track of the minimum and maximum values. Each time you push a new value onto the main stack, compare it with the current minimum and maximum values and update the auxiliary stacks accordingly.
2. **Constant Time Operations**: Ensure that each operation (push, pop, peek, get_min, get_max) runs in constant time by maintaining the auxiliary stacks properly during push and pop operations.
3. **Edge Cases**: Handle edge cases such as popping from an empty stack or getting the minimum/maximum from an empty stack gracefully, possibly by raising exceptions or returning sentinel values.
## Constraints
- The stack can contain integer values.
- The stack should handle a large number of operations efficiently.
## Complexity Analysis
- **Time Complexity**: Each operation (push, pop, peek, get_min, get_max) runs in O(1) time.
- **Space Complexity**: The space complexity is O(n) in the worst case, where n is the number of elements in the stack, due to the auxiliary stacks used for tracking minimum and maximum values.
