# Recursive Solution
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item
    being represented by a list
"""

# We will use `deepcopy()` function from the `copy` module
import copy


def permute(inputList):
    # A compound list to be returned
    finalCompoundList = []

    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])

    else:
        # Pick one element to be permuted
        first_element = inputList[0]
        # Take rest of the elements in a list
        rest_list = inputList[1:]

        # Recursive function call
        sub_compoundList = permute(rest_list)

        # Iterate through all lists of the compoundList
        #   returned from previous call
        for aList in sub_compoundList:

            # Permuted the `first_element` at all positions
            #   0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1):

                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)

                # A new list with size +1 as compared to aList is created
                #   by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)

                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)

    return finalCompoundList


# Test Cases
"""
Return True if output and expected_output
contains the same lists, False otherwise.

Note that the ordering of the list is not important.

Examples:
    check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

Args:
    output(list): list of list
    expected_output(list): list of list

Returns:
    bool
"""


def test(input, expected_output):
    output = permute(input)
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    print("Pass" if o == e else "Fail")


input1 = []
output1 = [[]]

input2 = [0]
output2 = [[0]]

input3 = [0, 1]
output3 = [[0, 1], [1, 0]]

intput4 = [0, 1, 2]
output4 = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

test(input1, output1)
test(input2, output2)
test(input3, output3)
test(intput4, output4)
