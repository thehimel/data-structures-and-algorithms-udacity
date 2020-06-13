# Singly Linked Lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return

    def remove(self, value):
        if self.head is None:
            return None

        if self.head.value == value:
            self.head = self.head.next
            return value

        previous = self.head
        current = previous.next

        while(current):
            if current.value == value:
                previous.next = current.next
                return value
            previous = current
            current = current.next

    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            out_string += str(node.value) + " -> "
            node = node.next
        out_string += 'None'  # Indicate the end of linked list
        return out_string


# 1 -> 2 -> 4
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)
print(linked_list)

print(linked_list.remove(10))
print(linked_list)

print(linked_list.remove(4))
print(linked_list)

linked_list.append(5)
print(linked_list)
