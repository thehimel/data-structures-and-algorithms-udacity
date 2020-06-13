"""
Problem statement
Given a sorted array that may have duplicate values,
use binary search to find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6]
and the given value is 3, the answer will be [4, 6]
(because the value 3 occurs first at index 4 and last at index 6 in the array).

The expected complexity of the problem is  O(log(n)) .
"""


def first_and_last_index(arr, target):
    # search first occurence
    first_index = find_start(arr, target, 0, len(arr) - 1)

    # search last occurence
    last_index = find_end(arr, target, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start(arr, target, start, end):
    # binary search solution to search for the first index of the array
    if start > end:
        return -1

    mid = start + (end - start)//2

    if arr[mid] == target:
        start_pos = find_start(arr, target, start, mid - 1)
        if start_pos != -1:
            return start_pos
        else:
            return mid

    elif arr[mid] < target:
        return find_start(arr, target, mid + 1, end)
    else:
        return find_start(arr, target, start, mid - 1)


def find_end(arr, target, start, end):
    # binary search solution to search for the last index of the array
    if start > end:
        return -1

    mid = start + (end - start)//2

    if arr[mid] == target:
        end_pos = find_end(arr, target, mid + 1, end)
        if end_pos != -1:
            return end_pos
        else:
            return mid

    elif arr[mid] < target:
        return find_end(arr, target, mid + 1, end)
    else:
        return find_end(arr, target, start, mid - 1)


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
target = 1
solution = [0, 0]
test_case_1 = [input_list, target, solution]
test_function(test_case_1)
input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
target = 3
solution = [3, 6]
test_case_2 = [input_list, target, solution]
test_function(test_case_2)
input_list = [0, 1, 2, 3, 4, 5]
target = 5
solution = [5, 5]
test_case_3 = [input_list, target, solution]
test_function(test_case_3)
input_list = [0, 1, 2, 3, 4, 5]
target = 6
solution = [-1, -1]
test_case_4 = [input_list, target, solution]
test_function(test_case_4)
