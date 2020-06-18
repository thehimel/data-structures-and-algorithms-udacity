"""
Coin Change

You are given coins of different denominations and a total amount of money.
Write a function to compute the fewest coins needed to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

As an example:
Input: coins = [1, 2, 3], amount = 6
Output: 2

Explanation: The output is 2 because we can use 2 coins with value 3.
That is, 6 = 3 + 3. We could also use 3 coins with value 2
(that is, 6 = 2 + 2 + 2), but this would use more coins—and the problem
specifies we should use the smallest number of coins possible.


Solution Two
- We initiate F[Amount] to be float('inf') and F[0] = 0

- Let F[Amount] to be the min number of coins needed to get the Amount.

- If F[Amount] is reachable,
F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1).

- If F[Amount] is not reachable, F[Amount + coin] = F(Amount + coin).

Complexity Analysis:
C = Number of coins
A = Amount

TC: O(C^A) -> O(n^2)
SC: O(A) -> O(n)

TC: O(n^2)
SC: O(n)
"""


def coin_change(coins, amount):
    # initiate the list with length amount + 1 and prefill with float('inf')
    res = [float('inf')]*(amount + 1)

    # when amount = 0, 0 number of coins will be needed for the change
    res[0] = 0

    i = 0
    while (i < amount):
        if res[i] != float('inf'):
            for coin in coins:
                if i <= amount - coin:
                    res[i+coin] = min(res[i] + 1, res[i+coin])

        i += 1

    if res[amount] == float('inf'):
        return -1

    return res[amount]


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1, 4, 5, 6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
