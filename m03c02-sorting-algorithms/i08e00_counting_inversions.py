"""
Counting Inversions
The number of inversions in a disordered list is the number of pairs of
elements that are inverted (out of order) in the list.

Here are some examples:

[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers,
for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j)
is called an inversion of arr.

Problem statement
Write a function, count_inversions, that takes an array (or Python list)
as input, and returns the total number of inversions present in the input.

Hint: Mergesort provides an efficient way to solve this problem.
"""


def count_inversions(arr):
    start = 0
    end = len(arr) - 1
    output = inversion_count_func(arr, start, end)
    return output


def inversion_count_func(arr, start, end):
    if start >= end:
        return 0

    mid = start + (end - start) // 2

    # find number of inversions in left-half
    left_answer = inversion_count_func(arr, start, mid)

    # find number of inversions in right-half
    right_answer = inversion_count_func(arr, mid + 1, end)

    output = left_answer + right_answer

    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(
        arr, start, mid, mid + 1, end)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    left_index = start_one
    right_index = start_two

    output_length = (end_two - start_two + 1) + (end_one - start_one + 1)
    output_list = [0 for _ in range(output_length)]
    index = 0

    while index < output_length:
        # if left <= right, it's not an inversion
        if arr[left_index] <= arr[right_index]:
            output_list[index] = arr[left_index]
            left_index += 1

        else:
            # left > right hence it's an inversion
            count = count + (end_one - left_index + 1)
            output_list[index] = arr[right_index]
            right_index += 1

        index = index + 1

        if left_index > end_one:
            for i in range(right_index, end_two + 1):
                output_list[index] = arr[i]
                index += 1
            break

        elif right_index > end_two:
            for i in range(left_index, end_one + 1):
                output_list[index] = arr[i]
                index += 1
            break

    index = start_one
    for i in range(output_length):
        arr[index] = output_list[i]
        index += 1
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
