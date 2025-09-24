# Happy Number

Write an algorithm to determine if a number `n` is happy.

A happy number is defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Example 2:**

```
Input: n = 2
Output: false
```

## Hints

1. Use a set to track numbers that have already been seen to detect cycles.
2. If you reach 1, return true; if you see a number again, return false.
3. Consider using a helper function to compute the sum of the squares of the digits of a number.
