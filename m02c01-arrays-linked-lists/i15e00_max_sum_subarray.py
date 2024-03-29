"""
Problem Statement
You have been given an array contaning numbers. Find and return the largest sum
in a contiguous subarray within the input array.

Example 1:
arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Output = [1, 2, 3, -4, 6]

Example 2:
arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
output = [1, 6]

Logic:
If current_sum + element is greater than the element, add it to the
current_sum_sub_arr. Else element is greater than the current_sum, create new
current_sum_sub_arr with only the element.

If current_sum is greater than the max_sum,
max_sum_sub_arr = current_sum_sub_arr
max_sum = current_sum

At last, return max_sum, max_sum_sub_arr as a tuple.

Complexity Analysis:
TC: O(n)
SC: O(n)
"""


def max_sum_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    current_sum_sub_arr = [arr[0]]
    max_sum_sub_arr = [arr[0]]

    # Traverse from index 1 to the end
    for i in range(1, len(arr)):
        element = arr[i]

        if current_sum + element > element:
            current_sum_sub_arr = current_sum_sub_arr + [element]
            current_sum += element
        else:
            current_sum_sub_arr = [element]
            current_sum = element

        if current_sum > max_sum:
            max_sum_sub_arr = current_sum_sub_arr
            max_sum = current_sum

    return max_sum, max_sum_sub_arr


def test(input, output):
    max_sum, max_sum_sub_arr = max_sum_subarray(input)
    print('Pass' if output == max_sum_sub_arr else 'Fail')


input = [1, 2, 3, -4, 6]
output = [1, 2, 3, -4, 6]
test(input, output)

input = [1, 2, -5, -4, 1, 6]
output = [1, 6]
test(input, output)

input = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
output = [15, -13, 14, -1, 2, 1]
test(input, output)
