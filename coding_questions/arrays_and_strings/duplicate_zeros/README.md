# Duplicate Zeros

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right. Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

### Example 1:

```
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

### Example 2:

```
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
```

### Constraints:

- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 9`

### Hints:

1. Try to come up with a solution that does not use any extra space.
2. A straightforward solution is to use a new array and iterate through the original array, copying elements to the new array and duplicating zeros as needed. However, this approach uses extra space.
3. To achieve an in-place solution, consider using two pointers to track the position of elements in the original array and the modified array.
4. Start from the end of the array and work backwards, which allows you to avoid overwriting elements that you still need to process.
