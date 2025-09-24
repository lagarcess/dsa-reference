import bisect


def smallestDifference(arrayOne, arrayTwo):
    # O(n log m) time | O(1) space
    arrayTwo.sort()
    smallest_diff = float("inf")
    smallest_pair = []

    for num1 in arrayOne:
        idx = bisect.bisect_left(arrayTwo, num1)

        if idx < len(arrayTwo):
            num2 = arrayTwo[idx]
            if abs(num1 - num2) < smallest_diff:
                smallest_diff = abs(num1 - num2)
                smallest_pair = [num1, num2]
        if idx > 0:
            num2 = arrayTwo[idx - 1]
            if abs(num1 - num2) < smallest_diff:
                smallest_diff = abs(num1 - num2)
                smallest_pair = [num1, num2]

    return smallest_pair
