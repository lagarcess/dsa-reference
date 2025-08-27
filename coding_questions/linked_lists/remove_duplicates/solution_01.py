def removeDuplicatesFromLinkedList(linkedList):
    # O(n) Time | O(1) Space
    currentNode = linkedList.head
    while currentNode is not None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    return linkedList
