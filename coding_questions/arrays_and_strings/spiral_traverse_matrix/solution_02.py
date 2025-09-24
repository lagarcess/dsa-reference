def spiralTraverse(array):
    # O(n) time | O(n) space - where n is the total number of elements in the array
    result = []
    # Call the recursive helper function with the initial boundaries
    spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralFill(array, startRow, endRow, startCol, endCol, result):
    # Base Case: If the pointers have crossed, stop the recursion
    if startRow > endRow or startCol > endCol:
        return

    # Traverse Right
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    # Traverse Down
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    # Traverse Left (with edge case check)
    if startRow < endRow:
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow][col])

    # Traverse Up (with edge case check)
    if startCol < endCol:
        for row in reversed(range(startRow + 1, endRow)):
            result.append(array[row][startCol])

    # Recursive Call: Call the function again for the inner spiral
    spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)
