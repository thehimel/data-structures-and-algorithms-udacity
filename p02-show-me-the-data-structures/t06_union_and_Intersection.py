class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node.value) + " -> "
            node = node.next
        out_string += 'None'  # Indicate the end of linked list
        return out_string


def copy_linked_list(llist, new_llist):
    node = new_llist.head
    while(node):
        llist.append(node.value)
        node = node.next


def union(llist_1, llist_2):
    llist = LinkedList()

    if llist_1.get_size() == 0:
        copy_linked_list(llist, llist_2)
        return llist
    else:
        copy_linked_list(llist, llist_1)

    if llist_2.get_size() == 0:
        return llist
    else:
        copy_linked_list(llist, llist_2)

    return llist


def is_present(llist, search_node):
    if llist.get_size() == 0:
        return False

    node = llist.head
    while node:
        if node.value == search_node.value:
            return True
        node = node.next

    return False


def intersection(llist_1, llist_2):
    llist = LinkedList()
    if llist_1.get_size() == 0 or llist_2.get_size() == 0:
        return llist  # Return an empty linked list

    node = llist_2.head
    while node:
        if is_present(llist_1, node):
            llist.append(node.value)
        node = node.next

    return llist


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1)
print(linked_list_2)
print(f'Union: {union(linked_list_1, linked_list_2)}')
print(f'Intersection: {intersection(linked_list_1, linked_list_2)}')
print()

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3)
print(linked_list_4)
print(f'Union: {union(linked_list_3, linked_list_4)}')
print(f'Intersection: {intersection(linked_list_3, linked_list_4)}')
print()
