from typing import List


def duplicateZeros(arr: List[int]) -> List[int]:
    # O(n) time | O(1) space
    zeros = arr.count(0)
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if i + zeros < n:
            arr[i + zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0
    return arr
