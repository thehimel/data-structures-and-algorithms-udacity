"""
A function that returns a boolean value indicating whether an element
is present, but with no information about the location of that element.

For example:
letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))  # True
print(contains('b', letters))  # False
"""


def search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end)//2
    mid_element = array[mid]

    if mid_element == target:
        return mid

    elif target < mid_element:
        end = mid - 1
        return search(array, target, start, end)

    else:
        start = mid + 1
        return search(array, target, start, end)


def recursive_binary_search(array, target):
    start = 0
    end = len(array) - 1
    return search(array, target, start, end)


def contains(array, target):
    index = recursive_binary_search(array, target)
    if index == -1:
        return False
    else:
        return True


letters = ['a', 'c', 'd', 'f', 'g']
print(contains(letters, 'a'))  # True
print(contains(letters, 'b'))  # False
