# y = target - x approach
def twoNumberSum(array, targetSum):
    # O(n) time | O(n) space
    nums_seen = set()
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums_seen:
            return [potentialMatch, num]
        nums_seen.add(num)
    return []
