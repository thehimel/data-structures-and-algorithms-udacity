"""
Task 2: Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.
Example: [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2]

You are given a target value to search. If found in the array return its index,
otherwise return -1. You can assume there are no duplicates in the array and
your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0, Output: 4
Here is some boilerplate code and test cases to start with:

Solution:
---------
Base condition is if mid_item == target, return mid.

Else if left_item is less than or equal to mid_item, that means left part
is uniformly increasing. Else, the right part is uniformly increasing.

If left part is uniformly increasing, and left_item <= target <= mid_item,
right = mid - 1 else left = mid + 1.

If right part is uniformly increasing, and mid_item <= target <= right_item,
left = mid + 1, else right = mid - 1.

Complexity Analysis:
Using the same logic of Binary search and diving the search portion in 2 halves
at every pass. Taking no extra space. Thus, in-place algorithm.

TC: O(log(n))
SC: O(1)
"""


def rotated_array_search(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        left_item = arr[left]
        right_item = arr[right]

        mid = (left + right) // 2
        mid_item = arr[mid]

        if (mid_item == target):
            return mid

        elif (left_item <= mid_item):
            if(left_item <= target and target <= mid_item):
                right = mid - 1
            else:
                left = mid + 1

        else:
            if(mid_item <= target and target <= right_item):
                left = mid + 1
            else:
                right = mid - 1

    return -1


def linear_search(arr, number):
    for index, element in enumerate(arr):
        if element == number:
            return index
    return -1


def test_function(test_case):
    arr = test_case[0]
    number = test_case[1]
    if linear_search(arr, number) == rotated_array_search(arr, number):
        print("Pass")
    else:
        print("Fail")


test_function([[], 20])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
