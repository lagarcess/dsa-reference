def isMonotonic(array):
    # O(N) time | O(1)
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        # If the direction was initially flat, find the first real trend
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        # Check if the current direction breaks the established trend
        if breaks_direction(direction, array[i - 1], array[i]):
            return False

    return True


def breaks_direction(direction, previous_int, current_int):
    difference = current_int - previous_int
    if direction > 0:
        return difference < 0  # Trend is increasing, but we found a decrease
    return difference > 0  # Trend is decreasing, but we found an increase
