"""
Longest Common Subsequence with Dynamic Programming


In text analysis, it is often useful to compare the similarity of two texts
E.g. Determine plagiarism between a source and answer text).
Longest Common Subsequence (LCS) is one measure of text similarity.

The Longest Common Subsequence is the longest sequence of letters that are
present in both the given two strings in the same relative order.

Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'.
The LCS will be 'ABD' with the length as 3 letters. It is because each of the
letters 'A' , 'B', and 'D' are present in both the given two strings in the
same relative order.

Note that:
- An LCS need not necessarily be a contiguous substring.
- There can be more than one LCS present in the given two strings.
- There can be many more common subsequences present here, with smaller length.
But, in this problem we are concerned with the longest common subsequence.

Complexity Analysis:
The time complexity of this implementation is dominated by the 2 nested loops,
Let the length of string_a and string_b is `n` and `m` respectively.
This would lead to a time complexity of O(n*m).
But, in general, we can consider it as O(n*n) -> O(n^2) instead of O(n*m).
"""


def lcs(string_a, string_b):

    # initialize the matrix
    b = len(string_b) + 1
    a = len(string_a) + 1
    lookup_table = [[0] * b] * a

    # enumerate(str) returns a tuple containing the index and character
    # in each iteration
    for char_a_i, char_a in enumerate(string_a):

        for char_b_i, char_b in enumerate(string_b):

            # If there is a match, fill that grid cell with the value
            # to the top-left of that cell plus one
            if char_a == char_b:
                value = lookup_table[char_a_i][char_b_i] + 1
                lookup_table[char_a_i + 1][char_b_i + 1] = value

            # If there is not a match, take the maximum value from either
            # directly to the left or the top cell
            else:
                left_cell = lookup_table[char_a_i][char_b_i + 1]
                top_cell = lookup_table[char_a_i + 1][char_b_i]
                max_value = max(left_cell, top_cell)

                lookup_table[char_a_i + 1][char_b_i + 1] = max_value

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]


# Test cell
# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"
lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"
lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1 == 5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2 == 7, "Incorrect LCS value."
print('Tests passed!')
