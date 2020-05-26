class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list_better(input_list):

    head = None
    tail = None

    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head  # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(value)  # attach the new node to the `next` of tail
            tail = tail.next  # update the tail

    return head


# Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
