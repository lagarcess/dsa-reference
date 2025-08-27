def middleNode(linkedList):
    # Two-pointers
    # O(n) time | O(s) space
    fast_pointer = slow_pointer = linkedList.head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer
