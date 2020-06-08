"""
Problem Statement
Suppose there is a staircase that you can climb in either 1 step, 2 steps,
or 3 steps.
In how many possible ways can you climb the staircase if the staircase has
n steps? Write a recursive function to solve the problem.

Example:

n == 1 then answer = 1

n == 3 then answer = 4

The output is 4 because there are four ways we can climb the staircase:

1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps
n == 5 then answer = 13
"""


# Solution
## Read input as specified in the question.
## Print output as specified in the question.

def staircase(n):
    if n <= 0:
        return 1

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


def test(n, solution):
    print("Pass" if solution == staircase(n) else "Fail")


n = 3
solution = 4
test(n, solution)

n = 4
solution = 7
test(n, solution)

n = 7
solution = 44
test(n, solution)
