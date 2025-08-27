def removeDuplicatesFromLinkedList(linkedList):
    # O(n) Time | O(1) Space
    currentNode = linkedList.head
    while currentNode is not None and currentNode.next is not None:
        if currentNode.value == currentNode.next.value:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
    return linkedList
