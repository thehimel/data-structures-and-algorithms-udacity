"""
Case Specific Sorting of Strings

Problem statement
Given a string consisting of uppercase and lowercase ASCII characters,
write a function, case_sort, that sorts uppercase and lowercase letters
separately, such that if the i-th place in the original string had an
uppercase character then it should not have a lowercase character after
being sorted and vice versa.

For example:
Input: helloWORLDbro
Output: behllDLORWoor

Solution:
Our input is an unsorted string. E.g. 'helloWORLDbro'
sorted_string = sorted(string)
sorted_string = ['D', 'L', 'O', 'R', 'W', 'b', 'e', 'h', 'l', 'l','o','o','r']
This is a list.

The ASCII values of capital letters are lower than the smaller letters.
Thus the capital letters are sorted first, and then the smaller letters.

Let's take an empty list, output = list()
We already have our sorted string. And for each lower case and upper case
letters in the input string, we just need to append letters
from the sorted list to the output list.

At last create a string from the list with the "".join(output)
"""


def case_sort(string):
    upper_ch_index = 0
    lower_ch_index = 0

    sorted_string = sorted(string)

    # Catch the first lower-case index from the sorted string list
    for index, character in enumerate(sorted_string):
        # ASCII value of a = 97 & ASCII value of z = 122
        # check if character is lower-case
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:
            lower_ch_index = index
            break

    output = list()
    # Copy from the sorted string list and append to the output accordingly
    for character in string:
        ascii_int = ord(character)
        # if character is lower case pick next lower_case character
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1

    return "".join(output)


def test(input, output):
    print('Pass' if case_sort(input) == output else 'Fail')


input = 'helloWORLDbro'
output = "behllDLORWoor"
test(input, output)
