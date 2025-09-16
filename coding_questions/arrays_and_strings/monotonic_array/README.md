# Monotonic Array

Write a function that takes in an array of integers and returns a boolean indicating whether the array is monotonic. An array is considered monotonic if it is either entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

## Example

```
array = [ -1, -5, -10, -1100, -1100, -1101, -1102, -9001]
```

## Sample Output

```true

```

## Hints

1. **Check Direction**: Start by determining the initial direction of the array (increasing or decreasing) by comparing the first two different elements.
2. **Single Pass**: Traverse the array once, checking if each element adheres to the identified direction. If any element violates the direction, return false.
3. **Edge Cases**: Consider edge cases such as arrays with all identical elements, arrays with only one element, or empty arrays.

### Optimal Space & Time Complexity

- **Time Complexity**: O(n), where n is the number of elements in the array. The array is traversed once.
- **Space Complexity**: O(1), since no additional space is used that scales with input size.
