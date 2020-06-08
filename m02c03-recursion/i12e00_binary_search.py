"""
Binary Search
Given a sorted list (say arr), and a key (say target).
The binary search algorithm returns the index of the target element
if it is present in the given arr list, else returns -1.

Here is an overview of how the the recursive version of
binary search algorithm works:

1. Given a list with the lower bound (start_index) and
    the upper bound (end_index).
2. Find the center (say mid_index) of the list.
    a. Check if the element at the center is your target?
        If yes, return the mid_index.

    b. Check if the target is greater than that element at mid_index?
        If yes, call the same function with right sub-array w.r.t center i.e.,
        updated indexes as mid_index + 1 to end_index

    c. Check if the target is less than that element at mid_index?
        If yes, call the same function with left sub-array w.r.t center i.e.,
        updated indexes as start_index to mid_index - 1

3. Repeat the step above until you find the target or until the bounds
    are the same or cross (the upper bound is less than the lower bound).

Complexity Analysis:
TC: O(log(n))
SC: O(1)
"""


def search(arr, target):
    return binary_search(arr, 0, len(arr)-1, target)


def binary_search(arr, start, end, target):
    if start > end:
        return -1

    mid = (start + end)//2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, start, mid-1, target)
    else:
        return binary_search(arr, mid+1, end, target)


arr = [0, 1, 22, 25, 28, 32, 36, 45, 95, 62]
print(search(arr, 32))
