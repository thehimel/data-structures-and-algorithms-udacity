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
        return False

    mid = (start + end)//2
    mid_element = array[mid]

    if mid_element == target:
        return True

    elif target < mid_element:
        end = mid - 1
        return search(array, target, start, end)

    else:
        start = mid + 1
        return search(array, target, start, end)


def contains(array, target):
    start = 0
    end = len(array) - 1
    return search(array, target, start, end)


letters = ['a', 'c', 'd', 'f', 'g']
print(contains(letters, 'a'))  # True
print(contains(letters, 'b'))  # False
