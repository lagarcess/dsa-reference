def isMonotonic(array):
    # O(N) time | O(1)
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            is_non_decreasing = False
        if array[i] > array[i - 1]:
            is_non_increasing = False

    return is_non_decreasing or is_non_increasing
