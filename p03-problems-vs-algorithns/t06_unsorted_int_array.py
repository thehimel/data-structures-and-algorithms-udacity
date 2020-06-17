"""
Task 6: Unsorted Integer Array
Max and Min in an Unsorted Array
In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. Do not use Python's
inbuilt functions to find min and max.


Args: ints(list): list of integers containing one or more integers
Return: a tuple(min, max) out of list of unsorted integers.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
Sorting usually requires O(n log n) time Can you come up with a O(n) algorithm
(i.e., linear time)?

Solution:
Assume the first item is the min_item and max_item.
Traverse throug the input, and if you find any better value update them.

Complexity Analysis:
TC: O(n)
SC: O(1)
In-place algorithm.
"""


def get_min_max(arr):
    if len(input) == 0:
        return None

    min_item = arr[0]
    max_item = arr[0]

    for i in range(len(arr)):
        item = arr[i]
        if item < min_item:
            min_item = item
        if item > max_item:
            max_item = item

    return (min_item, max_item)


def test(input, output):
    print('Pass' if get_min_max(input) == output else 'Fail')


# Test General Cases
input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
output = (0, 9)
test(input, output)

input = [25, 0, 145, 59, 61, 999, 55]
output = (0, 999)
test(input, output)

input = [-10, -100, -99, 0, -50, -999]
output = (-999, 0)
test(input, output)

# Test edge cases
input = []
output = None
test(input, output)
