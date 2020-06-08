"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Complexity Analysis of this solution:
Time complexity : O(2^n). Size of recursion tree will be 2^n.
Space complexity : O(n). The depth of the recursion tree can go upto n.
"""


def staircase(n):
    if n <= 0:
        return 1

    if n == 1:
        return 1
    elif n == 2:
        return 2

    return staircase(n - 1) + staircase(n - 2)


def test(n, solution):
    print("Pass" if solution == staircase(n) else "Fail")


n = 2
solution = 2
test(n, solution)

n = 3
solution = 3
test(n, solution)

n = 5
solution = 8
test(n, solution)

n = 8
solution = 34
test(n, solution)

n = 8
print(staircase(n))
