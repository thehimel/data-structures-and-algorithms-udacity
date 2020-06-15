"""
Problem Statement
Write a function that takes an input array (or Python list) consisting of
only 0s, 1s, and 2s, and sorts that array in a single traversal.

Input: [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
Output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

Note: If we can get the function to put the 0s and 2s in the correct positions,
this will aotumatically cause the 1s to be in the correct positions as well.

The idea is to put 0 and 2 in their correct positions, which will make sure
all the 1s are automatically placed in their right positions

Solution: Initialize next_pos_0 to the first index and next_pos_2
to the last index. We'll keep the 0's at the beginning and 2's at the ending.
Thus. 1's will stay in the middle.

We search of 0 and 2. If we find a 0, we bring it to it's next_pos_0.
If we find a 2, we throw it to it's next_pos_2. For both operations, we swap
the values in thoses indexes.

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


def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [
    2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2,
    1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
