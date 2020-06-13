"""
Find First
The binary search function is guaranteed to return an index for the element
you're looking for in an array, but what if the element appears more than once?

Consider this array:
[1, 3, 5, 7, 7, 7, 8, 11, 12]

Let's find the first occurrence of number 7:
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


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None
