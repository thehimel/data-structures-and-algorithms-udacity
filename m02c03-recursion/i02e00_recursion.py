# Recursive function power_of_2, which calculates 2^n .
def power_of_2(n):
    if n == 0:
        return 1

    return 2 * power_of_2(n - 1)


print('Pass' if power_of_2(5) == 32 else 'Fail')

"""
Call Stack
...
    -> power_of_2(5)
        -> power_of_2(4)
            -> power_of_2(3)
                -> power_of_2(2)
                    -> power_of_2(1)
                        -> power_of_2(0)
"""


# Implement sum_integers(n) to calculate the sum of all integers from  1 to n
# using recursion. For example, sum_integers(3) should return 6 = (1+2+3).
def sum_integers(n):
    if n == 1:
        return 1

    return n + sum_integers(n-1)


print('Pass' if sum_integers(3) == 6 else 'Fail')


# Slicing
# Let's look at an example of a recursive function that takes the sum of all
# numbers in an array. For example, the array of [5, 2, 9, 11] would sum to
# 27 = (5 + 2 + 9 + 11).

def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


arr = [1, 2, 3, 4]
print('Pass' if sum_array(arr) == 10 else 'Fail')

"""
Looking at this, you might think it has a running time of O(n), but that isn't
correct due to the slice operation array[1:]. This operation will take O(k)
time to run where k is the number of elements to copy. So, this function is
actually O(k∗n) running time complexity and O(k∗n) space complexity.
"""


# https://youtu.be/-tqsxDpp6NI
# Instead of slicing, we can pass the index for the element that we want
#   to use for addition.
def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)


arr = [1, 2, 3, 4]
print('Pass' if sum_array_index(arr, 0) == 10 else 'Fail')

"""
The function sum_array is a polynomial and sum_array_index is linear.
TC: O(n)
SC: O(n)
"""


# However, in our pursuit to use recursion we actually made things worse.
# Let's look at an iterative solution to this problem:
def sum_array_iter(array):
    result = 0

    for x in array:
        result += x

    return result


arr = [1, 2, 3, 4]
print('Pass' if sum_array_iter(arr) == 10 else 'Fail')

"""
The sum_array_iter function is a lot more straightforward than the
2 recursive functions, which is important. Second, to help ensure an answer
that is correct and bug free, pick the solution that is more readable.
In some cases recursion is more readable and in some cases iteration is more
readable. An Intuition for code readability can be gained by reading
other people’s code.
"""
