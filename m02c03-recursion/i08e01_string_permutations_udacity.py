"""
Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
"""

# Recursive Solution
"""
Param - input string
Return - compound object: list of all permutations of the input string
"""


def permutations(string):
    return return_permutations(string, 0)


def return_permutations(string, index):
    # output to be returned
    output = list()

    # Terminaiton / Base condition
    if index >= len(string):
        return [""]

    # Recursive function call
    small_output = return_permutations(string, index + 1)

    # Pick a character
    current_char = string[index]

    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:

        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):

            # Make use of the sub-string of previous output, to create a new sub-string.
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)

    return output


# Test
def test(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test(test_case)
