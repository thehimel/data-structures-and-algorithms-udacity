"""
Problem statement
Given an array arr and a target element target,
find the last index of occurence of target in arr using recursion.
If target is not present in arr, return -1.

For example:
For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6
For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1
"""


def last_index(arr, target):
    # we start looking from the last index
    return get_last_index(arr, target, len(arr) - 1)


def get_last_index(arr, target, index):
    if index < 0:
        return -1

    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return get_last_index(arr, target, index - 1)


def test(arr, target, solution):
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print(f"FAIL: Expected: {solution}, but you have got: {output}")


arr = [1, 2, 5, 5, 4]
target = 5
solution = 3
test(arr, target, solution)

arr = [1, 2, 5, 5, 4]
target = 7
solution = -1
test(arr, target, solution)

arr = [91, 19, 3, 8, 9]
target = 91
solution = 0
test(arr, target, solution)

arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5
test(arr, target, solution)
