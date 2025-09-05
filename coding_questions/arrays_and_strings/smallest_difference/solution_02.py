def smallestDifference(arrayOne, arrayTwo):
    # O(n*m) time | O(1)
    smallest_diff = float("inf")
    smallest_pair = []

    for num1 in arrayOne:
        for num2 in arrayTwo:
            current_diff = abs(num1 - num2)
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                smallest_pair = [num1, num2]

    return smallest_pair
