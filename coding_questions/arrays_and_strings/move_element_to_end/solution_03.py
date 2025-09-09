def moveElementToEnd(array, toMove):
    # O(n log n) time | O(1) or O(n)
    array.sort(key=lambda x: x == toMove)
    return array
