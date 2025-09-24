def threeNumberSum(array, targetSum):
    # O(N^2) time | O(n) space
    sorted_array = sorted(array)
    triplets = []

    for idx, num in enumerate(sorted_array):
        left = idx + 1
        right = len(array) - 1
        while left < right:
            currentSum = num + sorted_array[left] + sorted_array[right]
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum == targetSum:
                triplets.append([num, sorted_array[left], sorted_array[right]])
                left += 1
                right -= 1
    return triplets
