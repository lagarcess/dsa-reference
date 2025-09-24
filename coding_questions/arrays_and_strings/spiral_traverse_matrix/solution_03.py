def spiralTraverse(matrix):
    # O(n) time | O(N) space
    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # Traverse Right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # Traverse Down
        if top <= bottom:  # Check if rows remain
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

        # Traverse Left
        if top <= bottom:  # Check if rows remain
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # Traverse Up
        if left <= right:  # Check if rowscolumns remain
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result
