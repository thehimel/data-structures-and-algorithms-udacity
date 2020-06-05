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


# Test
def test(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permute(string)

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
