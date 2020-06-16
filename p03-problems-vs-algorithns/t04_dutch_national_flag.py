"""
Task 4: Dutch National Flag Problem

Given an input array consisting on only 0, 1, and 2.
Sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal.
For e.g. if you traverse the array twice, that would still be an O(n) solution
but it will not count as single traversal.


Solution:
Put 0s and 2s in their correct positions,
then 1s are automatically placed in their right positions.

Initialize next_pos_0 to the first index and next_pos_2
to the last index. We'll keep the 0's at the beginning and 2's at the ending.
Thus. 1's will stay in the middle.

We search of 0 and 2. If we find a 0, we bring it to it's next_pos_0.
If we find a 2, we throw it to it's next_pos_2. For both operations, we swap
the values in thoses indexes.

Complexity Analysis:
TC: O(n)
SC: O(1)
In-place algorithm.
"""


def sort_012(input_list):
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test edge cases
test_function([])
test_function([1])

# General Tests
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])

test_function(
    [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2,
        1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
