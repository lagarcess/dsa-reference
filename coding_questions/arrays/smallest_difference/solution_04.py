# Part 1: Merge Sort (Sorting from Scratch)
def merge_sort(array):
    if len(array) <= 1:
        return array

    middle_idx = len(array) // 2
    left_half = merge_sort(array[:middle_idx])
    right_half = merge_sort(array[middle_idx:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array


# Part 2: Binary Search (Finding the closest number)
def binary_search_closest(sorted_array, target):
    left, right = 0, len(sorted_array) - 1
    closest_idx = -1
    min_diff = float("inf")

    while left <= right:
        mid = (left + right) // 2
        current_diff = abs(sorted_array[mid] - target)

        if current_diff < min_diff:
            min_diff = current_diff
            closest_idx = mid

        if sorted_array[mid] < target:
            left = mid + 1
        elif sorted_array[mid] > target:
            right = mid - 1
        else:
            return mid  # Exact match found

    return closest_idx


# Part 3: The Main Function
def smallestDifference(arrayOne, arrayTwo):
    # Use the from-scratch merge_sort
    sorted_arrayTwo = merge_sort(arrayTwo)

    smallest_diff = float("inf")
    smallest_pair = []

    for num1 in arrayOne:
        # Use the from-scratch binary_search to find the closest number
        closest_idx = binary_search_closest(sorted_arrayTwo, num1)

        if closest_idx == -1:
            continue

        num2 = sorted_arrayTwo[closest_idx]
        current_diff = abs(num1 - num2)

        if current_diff < smallest_diff:
            smallest_diff = current_diff
            smallest_pair = [num1, num2]

    return smallest_pair
