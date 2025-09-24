# Spiral Traverse Matrix

Write a function that takes in an `n x m` two-dimensional array (that can be squared-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited.

## Sample Input

```
array = [
  [1, 2, 3],
  [12, 13, 4],
  [11, 14, 5],
  [10, 15, 6],
  [9, 8, 7],
]
```

## Sample Output

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

## Hints

1. You can solve this problem by simulating the process of traversing the array in a spiral order. You can keep track of the boundaries of the unvisited elements and adjust them as you traverse the array.
2. You can also solve this problem recursively by defining a helper function that takes in the current boundaries of the unvisited elements and appends the elements in spiral order to the result array.
3. Another approach is to use a direction vector to represent the four possible directions (right, down, left, up) and iterate through the array while changing direction when you hit a boundary or a previously visited element. (not recommended)
