# Remove Duplicate from Sorted Array

Given an integer array `nums` sorted in **non-decreasing** order, remove the duplicates in-place such that each element appears only once and returns the new length of the array. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- change the array `nums` such that the first `k` elements are unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as wel as the size of `nums`.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

**Constraints**

- 1 <= nums.length <= 3 \* 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
