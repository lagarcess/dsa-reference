# Brute Force Approach
def twoNumberSum(array, targetSum):
    # O(n^2) time | O(1) space
    n = len(array)

    for i in range(n - 1):
        for j in range(i + 1, n):
            currentSum = array[i] + array[j]
            if currentSum == targetSum:
                return [array[i], array[j]]
    return []
