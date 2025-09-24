def moveElementToEnd(array, toMove):
    # O(n log n) time | O(1) or O(n), keeps order of other elements
    array.sort(key=lambda x: x == toMove)
    return array
