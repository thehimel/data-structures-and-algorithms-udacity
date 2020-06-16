"""
Task 1: Square Root of an Integer

Find the square root of the integer without using any Python library.
You have to find the floor value of the square root.
For example, if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because,
sqrt(5) = 5.196 whose floor value is 5.

Args:
    number(int): Number to find the floored squared root
Returns:
    int: Floored Square Root

Logic: Use binary search for this operation.

Solution
--------
Base case:
mid_square = mid * mid
mid_next_square = (mid+1) * (mid+1)
if mid_square <= number and mid_next_square > number:
    return mid

If number < mid_square, search left, else search right.

Complexity Analysis:
At every step, we're dividing our search portion with binary search.
And we know, binary search has TC of O(log(n)).

TC: O(log(n))
SC: O(1)
"""


def sqrt(number):
    if number < 0:
        return

    if number == 0 or number == 1:
        return number

    start = 1
    end = number
    return binary_search(start, end, number)


def binary_search(start, end, number):
    mid = (start + end) // 2
    mid_square = mid * mid
    mid_next_square = (mid+1) * (mid+1)

    if mid_square <= number and mid_next_square > number:
        return mid

    elif number < mid_square:
        return binary_search(start, mid-1, number)
    else:
        return binary_search(mid+1, end, number)


print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")

print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (25 == sqrt(625)) else "Fail")
print("Pass" if (25 == sqrt(630)) else "Fail")
