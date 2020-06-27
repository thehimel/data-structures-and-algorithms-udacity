# Solution
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Append a value to the Linked List in ascending sorted order

Args:
    value(int): Value to add to Linked List
"""


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        return None


"""
Given an array of integers,
    use SortedLinkedList to sort them and return a sorted array.

Args:
    array(array): Array of integers to be sorted
Returns:
    array: Return sorted array
"""


def sort(array):
    sorted_array = []

    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append(value)

    # Convert sorted linked list to a normal list/array
    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next

    return sorted_array


# Test
linked_list = SortedLinkedList()
linked_list.append(3)
print("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print("Pass" if (node.value == 4) else "Fail")

# Main test
print("Pass" if (
    sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")
