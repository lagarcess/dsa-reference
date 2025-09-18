# Move Element to End

You're given an array of integers and a specific integer. Write a function that moves all instances of that integer in the array to the end of the array and returns the modified array.

The function should perform this operation in place (i.e., without creating a new array) and doesn't need to maintain the relative order of the other integers.

### Sample Input

```python
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
```

### Sample Output

```python
[1, 3, 4, 5, 2, 2, 2]
```

### Hints

1. **Two-Pointer Technique**: Use two pointers to traverse the array. One pointer can track the position to place non-target elements, while the other pointer scans through the array.
2. **In-Place Swapping**: When the scanning pointer finds a non-target element, swap it with the element at the position of the first pointer and then move both pointers forward.
3. **Edge Cases**: Consider edge cases such as an empty array, an array with all elements being the target, or an array with no instances of the target.

### Optimal Space & Time Complexity

- **Time Complexity**: O(n), where n is the number of elements in the array. Each element is processed at most twice.
- **Space Complexity**: O(1), since the operation is performed in place without using additional storage for another array.
