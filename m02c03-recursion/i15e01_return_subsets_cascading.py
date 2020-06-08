"""
Approach 1: Cascading
Source: https://leetcode.com/problems/subsets/solution/

Complexity Analysis

Time complexity: O(N x 2^n) to generate all subsets and then copy them
into output list.

Space complexity: O(N x 2^n). This is exactly the number of solutions
for subsets multiplied by the number N of elements to keep for each subset.

For a given number, it could be present or absent (i.e. binary choice)
in a subset solution. As as result, for N numbers,
we would have in total 2^n choices (solutions).
"""


def subsets(nums):
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output


def test_function(arr, solution):
    print("Pass" if solution.sort() == subsets(arr).sort() else "Fail")


arr = [9]
solution = [[], [9]]
test_function(arr, solution)

arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_function(arr, solution)

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
test_function(arr, solution)
