"""
Use the following link to visualize the python codes to understand call stacks
"""


def add(num_one, num_two):
    output = num_one + num_two
    return output


result = add(5, 7)
print(result)


def add(num_one, num_two):
    output = num_one + num_two
    custom_print(output, num_one, num_two)
    return output


def custom_print(output, num_one, num_two):
    print("The sum of {} and {} is: {}".format(num_one, num_two, output))


result = add(5, 7)


"""
Problem Statement
Consider the following problem:

Given a positive integer n, write a function, print_integers,
that uses recursion to print all numbers from n to 1.

For example, if n is 4, the function shuld print 4 3 2 1.

If we use iteration, the solution to the problem is simple.
We can simply start at 4 and use a loop to print all numbers till 1.
However, instead of using an interative approach,
our goal is to solve this problem using recursion.

Complexity analysis:
TC: O(n)
SC: O(n)
"""


def print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)


print_integers(5)
