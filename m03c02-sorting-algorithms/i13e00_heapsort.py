"""
heapify(arr, n, i):
Using i as the index of the current node, find the 2 child nodes
(if the array were a binary tree) and find the largest value.
If one of the children is larger swap the values and recurse into that subree.
"""


def heapify(arr, n, i):
    # consider current index as largest
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


"""
heapsort(arr):
First convert the array into a maxheap by calling heapify on each node,
starting from the end. now that you have a maxheap, you can swap the first
element (largest) to the end (final position) and make the array minus
the last element into maxheap again.
Continue to do this until the whole array is sorted
"""


def heapsort(arr):

    n = len(arr)

    # Build a maxheap.
    # Traverse from n to 0
    for i in range(n, 0-1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    # Traverse from n-1 to 1
    for i in range(n-1, 1-1, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def test(input, output):
    heapsort(input)
    print('Pass' if input == output else 'Fail')


input = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
output = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test(input, output)

input = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
output = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test(input, output)

input = [99]
output = [99]
test(input, output)

input = [0, 1, 2, 5, 12, 21, 0]
output = [0, 0, 1, 2, 5, 12, 21]
test(input, output)

input = [0]
output = [0]
test(input, output)

input = []
output = []
test(input, output)
