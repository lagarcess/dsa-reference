class LinkedListNode:
    """Represents a node in a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Represents a singly linked list."""

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            for value in values:
                self.append(value)

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def getNodesInArray(self):
        """Returns a list of node values in the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(current.value)
            current = current.next
        return nodes
