from i07e00_simple_linked_list import head


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


print_linked_list(head)
