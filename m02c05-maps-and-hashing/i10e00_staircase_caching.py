""""
Problem Statement

A child is running up a staircase and can hop either 1 step, 2 steps or 3 steps
at a time. Given that the staircase has a total n steps, write a function to
count the number of possible ways in which child can run up the stairs.

For e.g.
n == 1 then answer = 1
n == 3 then answer = 4

The output is 4 because there are four ways we can climb the staircase:
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step
3 steps

n == 5 then answer = 13

Recursive Solution:
def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


Problem Statement - (Caching)
While using recursion for the above problem, you might have noticed a small
problem with efficiency. Let's take a look at an example.
Say the total number of steps are 5. This means that we will have to call at
(n=4), (n=3), and (n=2). To calculate the answer for n=4, we would have to call
(n=3), (n=2) and (n=1). You can notice that even for a small number of
staircases (here 5), we are calling n=3 and n=2 multiple times.
Each time we call a method, additional time is required to calculate the
solution. In contrast, instead of calling on a particular value of n again and
again, we can calculate it once and store the result to speed up our program.

"""


def staircase(n):
    return staircase_faster(n, {})


def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        else:
            first_output = staircase_faster(n - 1, num_dict)

        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        output = first_output + second_output + third_output

    num_dict[n] = output
    return output


def test_function(n, expected_output):
    print('Pass' if staircase(n) == expected_output else 'Fail')


test_function(4, 7)
test_function(5, 13)
test_function(3, 4)
test_function(20, 121415)
