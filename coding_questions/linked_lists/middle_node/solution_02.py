def middleNode(linkedList):
    # Array-appraoch
    nodes = []
    current = linkedList.head
    while current:
        nodes.append(current)
        current = current.next

    middle_idx = len(nodes) // 2
    return nodes[middle_idx]
