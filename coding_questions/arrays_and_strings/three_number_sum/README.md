# three_number_sum

Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return an empty array.

## Sample Input

```python
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
```

## Sample Output

```python
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
```

## Hints

1. You can solve this problem using a hash map to store the numbers you've seen so far.
2. Consider using a two-pointer approach after sorting the array.
3. Don't forget to handle duplicate triplets in your final output.
4. Think about the time complexity of your solution and how sorting the array might help.
5. Make sure to test your function with edge cases, such as arrays with fewer than three numbers or arrays where no triplet sums to the target.

## Optimal Space & Time Complexity

O(n^2) time | O(n) space - where n is the length of the input array
