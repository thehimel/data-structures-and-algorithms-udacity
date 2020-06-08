"""
Solution using Fibinacci Numbers

Complexity Analysis

Time complexity : O(n).
Single loop upto n is required to calculate nth fibonacci number.

Space complexity : O(1). Constant space is used.
"""


def staircase(n):
    first = 1
    second = 1
    for i in range(2, n+1):
        third = first + second
        first = second
        second = third
    return second


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
