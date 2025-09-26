# Longest Peak

Write a function that takes in an array of integers and returns the length of the longest "peak" in the array.

A "peak" is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers `1, 4, 6, 2` form a peak, but the integers `4, 0, 10` do not and neither do the integers `1, 2, 2, 0`. Similarly, the integers `1, 2, 3` do not form a peak because there aren't any strictly decreasing integers after the 3.

### Sample Input

```python
array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
# Output: 6
# The longest peak is [0, 10, 6, 5, -1, -3]
```

### Sample Output

```python
6 # The longest peak is [0, 10, 6, 5, -1, -3]
```

### Hints

1. You can iterate through the array and identify potential peaks by checking if the current element is greater than its neighbors.
2. Once a peak is identified, you can expand outwards to count the length of the peak by moving left and right until the increasing and decreasing conditions are violated.
3. Keep track of the maximum peak length found during the iteration and return it at the end.

### Optimal Space & Time Complexity

- Time: O(n) - where n is the length of the input array. We traverse the array a constant number of times.
- Space: O(1) - we use a constant amount of space regardless of the input size.
