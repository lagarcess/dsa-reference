def threeNumberSum(array, targetSum):
    # O(n^3) time | O(n) space
    triplets = []
    n = len(array)
    array.sort()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if array[i] + array[j] + array[k] == targetSum:
                    triplets.append([array[i], array[j], array[k]])
    return triplets
