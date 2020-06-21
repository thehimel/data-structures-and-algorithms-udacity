"""
Flattening a nested linked list¶
Suppose you have a linked list where the value of each node is a sorted linked
list (i.e., it is a nested list). Your task is to flatten this nested list —
that is, to combine all nested lists into a single (sorted) linked list.

First, we'll need some code for generating nodes and a linked list:
"""


# A class behaves like a data-type, just like an int,
#   float or any other built-in ones.
# User defined class
# <-- For simple LinkedList, "value" argument will be an int, whereas,
#   for NestedLinkedList, "value" will be a LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
# <-- Expects "head" to be a Node made up of an int or LinkedList
class LinkedList:
    def __init__(self, head):
        self.head = head

    '''
    For creating a simple LinkedList,
        we will pass an integer as the "value" argument
    For creating a nested LinkedList,
        we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    # We will need this function to convert a LinkedList object
    #   into a Python list of integers
    # <-- Declare a Python list
    # <-- Create a temporary Node object
    def to_list(self):
        out = []
        node = self.head

        # <-- Iterate untill we have nodes available
        # <-- node.value is actually of type Node, therefore convert it into
        #   int before appending to the Python list
        while node:
            out.append(int(str(node.value)))
            node = node.next

        return out


"""Solution"""


# First, let's implement a merge function that takes in two linked lists
# and returns one sorted linked list. Note, this implementation expects
# both linked lists to be sorted.
def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


# Now let's implement flatten recursively using merge.
# In a NESTED LinkedList object, each node will be a simple LinkedList
# <-- self.head is a node for NestedLinkedList
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    # A recursive function
    def _flatten(self, node):

        # A termination condition
        # <-- First argument is a simple LinkedList
        if node.next is None:
            return merge(node.value, None)

        # _flatten() is calling itself till a termination condition is achieved
        # <-- Both arguments are a simple LinkedList each
        return merge(node.value, self._flatten(node.next))


# Test merge() function
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 3 5
    print(node.value)
    node = node.next


# Test flatten() function
# Create a nested linked list with one node.
# The node itself is a simple linked list as 1-->3-->5 created previously
nested_linked_list = NestedLinkedList(Node(linked_list))

# Append a node (a linked list as 2-->4) to the existing nested linked list
nested_linked_list.append(second_linked_list)

# Call the `flatten()` function
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next


""" Main test """


# First Test scenario
# Create a simple LinkedList
# <-- Notice that we are passing a Node made up of an integer
# <-- Notice that we are passing a numerical value as an argument
#   in the append() function here
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

# Create another simple LinkedList
second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

# Create a NESTED LinkedList, where each node will be
#   a simple LinkedList in itself
# <-- Notice that we are passing a Node made up of a simple LinkedList object
nested_linked_list = NestedLinkedList(Node(linked_list))
# <-- Notice that we are passing a LinkedList object in the append() function
nested_linked_list.append(second_linked_list)
