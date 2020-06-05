"""
Given an input string, find the list of strings that can be made
with the permutation of the input string.
input = 'abc'
output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""
"""
Easy solution:
TC: O(n!)
SC: O(n!)

Inspired by:
List Permutation Recusive DFS Solution by LeetCode user leetcode.com/caikehe
https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS)
"""


def permute(string):
    res = []
    dfs(string, '', res)
    return res


def dfs(string, path, res):
    print(f'\t--- dfs(string = {string}, path = {path}, res = {res})')

    if not string:
        res.append(path)

    for i in range(len(string)):
        dfs(string[:i] + string[i+1:], path+string[i], res)


def test(input, expected_output):
    output = permute(input)
    print('Pass' if output == expected_output else 'Fail')


input1 = 'ab'
output1 = ['ab', 'ba']
test(input1, output1)

input2 = 'abc'
output2 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
test(input2, output2)
