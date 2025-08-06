# Two-pass approach
# O(n) Time | O(1) Space
def middleNode(linkedList):
    count = 0
    current = linkedList.head
    while current is not None:
        count += 1
        current = current.next

    middle_idx = count // 2
    current = linkedList.head
    for _ in range(middle_idx):
        current = current.next

    return current
