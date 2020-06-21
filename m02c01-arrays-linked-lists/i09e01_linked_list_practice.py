"""
Linked List Practice
Implement a linked list class. You have to define a few functions that perform
the desirbale action. Your LinkedList class should be able to:

- Append data to the tail of the list and prepend to the head
- Search the linked list for a value and return the node
- Remove a node
- Pop, which means to return the first node's value
    and delete the node from the list
- Insert data at some position in the list
- Return the size (length) of the linked list
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Task 1. Write definition of `prepend()` function and test it
# Define the function outside of the class
# Prepend a node to the beginning of the list
def prepend(self, value):
    if self.head is None:
        self.head = Node(value)
        return

    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


# Task 2. Write definition of `append()` function and test it
# Append a node to the end of the list
# Here I'm not keeping track of the tail. It's possible to store the tail
# as well as the head, which makes appending like this an O(1) operation.
# Otherwise, it's an O(N) operation as you have to iterate through the
# entire list to add a new tail.
def append(self, value):
    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)


LinkedList.append = append

# Test append - 1 item
linked_list.prepend(2)
linked_list.append(3)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2 items
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"


# Task 3. Write definition of `search()` function and test it
# Search the linked list for a node with the requested value
# and return the node.
def search(self, value):
    if self.head is None:
        return None

    node = self.head
    while node:
        if node.value == value:
            return node
        node = node.next

    raise ValueError("Value not found in the list.")


LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


# #### Task 4. Write definition of `remove()` function and test it
def remove(self, value):
    """ Delete the first node with the desired data. """
    if self.head is None:
        return

    if self.head.value == value:
        self.head = self.head.next
        return

    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next

    raise ValueError("Value not found in the list.")


LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"


# #### Task 5. Write definition of `pop()` function and test its functionality
def pop(self):
    """ Return the first node's value and remove it from the list. """
    if self.head is None:
        return None

    node = self.head
    self.head = self.head.next

    return node.value


LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# #### Task 6. Write definition of `insert()` function and test it
def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
        length of the list, append to the end of the list. """
    # If the list is empty
    if self.head is None:
        self.head = Node(value)
        return

    if pos == 0:
        self.prepend(value)
        return

    index = 0
    node = self.head
    while node.next and index <= pos:
        if (pos - 1) == index:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return

        index += 1
        node = node.next
    else:
        self.append(value)


LinkedList.insert = insert

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"


# Task 7. Write definition of `size()` function and test its functionality
def size(self):
    """ Return the size or length of the linked list. """
    size = 0
    node = self.head
    while node:
        size += 1
        node = node.next

    return size


LinkedList.size = size

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
