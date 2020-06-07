"""
Problem Statement
Define a procedure, deep_reverse, that takes as input a list,
and returns a new list that is the deep reverse of the input list.

This means it reverses all the elements in the list,
and if any of those elements are lists themselves,
reverses all the elements in the inner list, all the way down.

Note: The procedure must not change the input list itself.

Example
Input: [1, 2, [3, 4, 5], 4, 5]
Output: [5, 4, [5, 4, 3], 2, 1]

Hint
Begin with a blank final list to be returned.
Traverse the given list in the reverse order.
If an item in the list is a list itself, call the same function.
Otheriwse, append the item to the final list.

Information regarding slice in python:
For a given list,
sample syntax are - myList[1:10:2], myList[:-1:1], myList[::-1]

The first argument is the starting index of the slice (inclusive),
second argument is the ending index of the slice (exclusive),
third argument is the increment/decrement step size.

If we do not specify an argument,
it means to consider all elements from that end of the list.
"""


# Recursive Solution
def deep_reverse(arr):

    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = []  # final list to be returned

    # Traverse the given list in the reverse direction using extended slice.
    for item in arr[::-1]:
        # If this item is a list itself,
        #   invoke deep_reverse to reverse the items recursively.
        if type(item) is list:
            item = deep_reverse(item)

        # append the item to the final list
        reversed_items.append(item)

    return reversed_items


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)
