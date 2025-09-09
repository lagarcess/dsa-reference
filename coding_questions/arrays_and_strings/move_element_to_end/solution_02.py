def moveElementToEnd(array, toMove):
    # O(n) space & time, not in-place
    others = []
    toMoveList = []

    for num in array:
        if num == toMove:
            toMoveList.append(num)
        else:
            others.append(num)
    return others + toMoveList
