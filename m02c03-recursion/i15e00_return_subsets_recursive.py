"""
Problem Statement
Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important.
However the order of elements in a particular subset should remain the
same as in the input array.

Note:
An empty set will be represented by an empty list. If there are
repeat integers, each occurrence must be treated as a separate entity.

Example 1

arr = [9, 9]
output = [[],
    [9],
    [9],
    [9, 9]]

Example 2

arr = [9, 12, 15]
output =  [[],
    [15],
    [12],
    [12, 15],
    [9],
    [9, 15],
    [9, 12],
    [9, 12, 15]]
"""


# Solution
def subsets(arr):
    return get_subsets(arr, 0)


def get_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = get_subsets(arr, index + 1)

    output = []
    # append existing subsets
    # add current elements to existing subsets and add them to the output
    for element in small_output:
        output.append(element)

        current = []
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = subsets(arr)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [9]
solution = [[], [9]]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2]
subsets(arr)
