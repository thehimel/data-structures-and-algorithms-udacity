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
Generally recursive binary search takes O(log(n)) space. But here our input
is not an array. And we are logically considering our input limit. Notice,
we don't have any array to hold the positions at every pass. Thus, the
algorithm is taking no extra space and it is an in-place algorithm.

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


def test(input, output):
    print("Pass" if sqrt(input) == output else "Fail")


# Test general cases
test(0, 0)
test(1, 1)
test(9, 3)
test(16, 4)
test(625, 25)
test(630, 25)

# Test edge cases
test(-1, None)
test(999999999999999, 31622776)
