def removeDuplicates(nums: list[int]) -> int:
    # Using extra space (less efficient)
    # O(n) space, O(n) time
    if not nums:
        return 0
    unique_numbers = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            unique_numbers.append(nums[i])
    # Optional, modifies the orginal input array
    for i in range(len(unique_numbers)):
        nums[i] = unique_numbers[i]
    return len(unique_numbers)