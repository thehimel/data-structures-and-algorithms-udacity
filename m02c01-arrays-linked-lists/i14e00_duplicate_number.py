"""
Problem Statement
You have been given an array of length = n. The array contains integers
from 0 to n - 2. Each number in the array is present exactly once
except for one number which is present twice.
Find and return this duplicate number present in the array

Example:
arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n)
and the expected space-complexity is O(1).

Notice carefully that
1. All the elements of the array are always non-negative
2. If array length = n, then elements would start from 0 to (n-2),
    i.e. Natural numbers 0,1,2,3,4,5...(n-2)
3. There is only SINGLE element which is present twice.

Therefore let's find the sum of all elements (current_sum)
    of the original array, and find the sum of first (n-2)
    Natural numbers (expected_sum).


Trick:
The second occurance of a particular number (say `x`)
is actually occupying the space that would have been utilized
by the number (n-1). This leads to:
expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
x = current_sum - expected_sum
Tada!!! :)

arr = [0, 1, 2, 3, 4, 5, 5]
n = 7, n-2 = 5
expected_sum = 0+1+2+3+4+5 = 15
current_sum = 0+1+2+3+4+5+5 = 20
x = 20-15 = 5

arr = [0, 1, 2, 3, 3, 4, 5]
n = 7, n-2 = 5
expected_sum = 0+1+2+3+4+5 = 15
current_sum = 0+1+2+3+3+4+5 = 18
x = 18-15 = 3


Traverse from 0 to (length of array-1) to get the expected_sum
Alternatively, you can use the formula for sum of
an Arithmetic Progression to get the expected_sum

The argument of range() functions are:
starting index [OPTIONAL], ending index (non exclusive),
    and the increment/decrement size [OPTIONAL]
It means that if the array length = n, loop will run form 0 to (n-2)
"""


def duplicate_number(arr):
    expected_sum = 0
    current_sum = 0

    # for (i=0; i<=n-2; i++)
    for i in range(len(arr) - 1):
        expected_sum += i

    for num in arr:
        current_sum += num

    # The difference between the
    return current_sum - expected_sum


# Test
def test(arr, output):
    print("Pass" if output == duplicate_number(arr) else "Fail")


arr = [0, 0]
output = 0
test(arr, output)

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3
test(arr, output)

arr = [0, 2, 3, 1, 4, 5, 5]
output = 5
test(arr, output)

arr = [0, 1, 5, 4, 3, 2, 0]
output = 0
test(arr, output)

arr = [0, 1, 5, 5, 3, 2, 4]
output = 5
test(arr, output)
