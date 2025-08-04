# Two Pointers Approach
def twoNumberSum(array, targetSum):
    # O(n log(n)) time | O(1) space
    array.sort()
    left = 0
    right = len(array)-1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
