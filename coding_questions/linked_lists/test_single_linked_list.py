import pytest
from .single_linked_list import LinkedList, LinkedListNode
# --- Pytest Fixtures ---
# Fixtures provide a fixed baseline for tests to run on.

@pytest.fixture
def empty_list():
    """Returns an empty LinkedList."""
    return LinkedList()

@pytest.fixture
def single_node_list():
    """Returns a LinkedList with a single node."""
    return LinkedList([10])

@pytest.fixture
def multi_node_list():
    """Returns a LinkedList with multiple nodes."""
    return LinkedList([1, 2, 3])

# --- Test Functions ---

def test_node_creation():
    """Tests that a LinkedListNode is created with the correct value and next pointer."""
    node = LinkedListNode(5)
    assert node.value == 5
    assert node.next is None

def test_list_initialization_empty():
    """Tests that a LinkedList can be initialized with no values."""
    ll = LinkedList()
    assert ll.head is None
    assert ll.tail is None

def test_list_initialization_with_values(multi_node_list):
    """Tests that a LinkedList is correctly initialized with a list of values."""
    ll = multi_node_list
    assert ll.head is not None
    assert ll.tail is not None
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.tail.value == 3
    assert ll.tail.next is None

def test_append_to_empty_list(empty_list):
    """Tests appending a value to an empty list."""
    ll = empty_list
    ll.append(5)
    assert ll.head is not None
    assert ll.tail is not None
    assert ll.head.value == 5
    assert ll.tail.value == 5
    assert ll.head == ll.tail  # Head and tail should be the same node

def test_append_to_non_empty_list(single_node_list):
    """Tests appending a value to a list that already has nodes."""
    ll = single_node_list
    ll.append(20)
    assert ll.head.value == 10
    assert ll.tail.value == 20
    assert ll.head.next is not None
    assert ll.head.next.value == 20
    assert ll.tail.next is None

def test_tail_pointer_after_multiple_appends(multi_node_list):
    """Tests that the tail pointer is correctly updated after multiple appends."""
    ll = multi_node_list
    ll.append(4)
    ll.append(5)
    assert ll.tail.value == 5
    assert ll.head.value == 1
    assert ll.tail.next is None