def moveElementToEnd(array, toMove):
    # O(1) space & O(n) time, in-place, keeps order of other elements
    writePoint = 0
    for num in array:
        if num != toMove:
            array[writePoint] = num
            writePoint += 1
    for i in range(writePoint, len(array)):
        array[i] = toMove
    return array
