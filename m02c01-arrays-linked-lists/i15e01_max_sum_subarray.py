"""
Problem Statement
You have been given an array containg numbers. Find and return the largest sum
in a contiguous subarray within the input array.

Example 1:
arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.

Example 2:
arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.

Logic:
1. We have to find the sum of "contiguous" subarray,
    therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes
    the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum`
    with the MAXIMUM of either:
    - The element added to the `current_sum` (denotes the addition of
        the element to the current subarray)
    - The element itself  (denotes the starting of a new subarray)
    - Update (overwrite) `max_sum`,
        if it is lower than the updated `current_sum`
4. Return `max_sum`

Complexity Analysis:
TC: O(n)
SC: O(n)
"""


def max_sum_subarray(arr):
    # `current_sum` denotes the sum of a subarray
    # `max_sum` denotes the maximum value of `current_sum` ever
    current_sum = arr[0]
    max_sum = arr[0]

    # Keeping the track of sub_arr is optional.
    # We are using it just to visualize
    current_sum_sub_array = max_sum_sub_arr = [arr[0]]
    print(f'current_sum_sub_array = {current_sum_sub_array}', end=', ')
    print(f'current_sum = {current_sum}')
    print(f'max_sum_sub_arr = {max_sum_sub_arr}', end=', ')
    print(f'max_sum = {max_sum}')

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        # Optional block start
        # This block is optional.
        # We are using it just to visualize
        if current_sum + element > element:
            current_sum_sub_array = current_sum_sub_array + [element]
        else:
            current_sum_sub_array = [element]
        print(f'current_sum_sub_array = {current_sum_sub_array}', end=', ')
        # Optional block end

        '''
        Compare (current_sum + element) vs (element)
        If (current_sum + element) is higher,
          it denotes the addition of the element to the current subarray
        If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)
        print(f'current_sum = {current_sum}')

        # Optional block start
        if current_sum > max_sum:
            max_sum_sub_arr = current_sum_sub_array
        print(f'max_sum_sub_arr = {max_sum_sub_arr}', end=', ')
        # Optional block end

        # Update (overwrite) `max_sum`,
        #   if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)
        print(f'max_sum = {max_sum}')

    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements
test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
test_case = [arr, solution]
test_function(test_case)
