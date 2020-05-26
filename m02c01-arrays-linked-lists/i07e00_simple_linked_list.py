class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list():
    head = Node(2)
    head.next = Node(1)

    # (2) -> (1) -> (4) -> (3) -> (5)
    head.next.next = Node(4)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(5)

    return head


def print_linked_list(head):
    print(head.value)
    print(head.next.value)
    print(head.next.next.value)
    print(head.next.next.next.value)
    print(head.next.next.next.next.value)


head = create_linked_list()

if __name__ == '__main__':
    print_linked_list(head)
