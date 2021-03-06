"""
Stock Prices
You are given access to yesterday's stock prices for a single stock.
The data is in the form of an array with the stock price in 30 minute
intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time.
With this data, write a function that returns the maximum profit obtainable.
You will need to buy before you can sell.

For example, suppose you have the following prices:
prices = [3, 4, 7, 8, 6]

Note: This is a shortened array, just for the sake of example—a full set of
prices for the day would have 13 elements (one price for each 30 minute
interval betwen 9:30 and 4:00), as seen in the test cases further down in this
notebook.

In order to get the maximum profit in this example, you would want to buy
at a price of 3 and sell at a price of 8 to yield a maximum profit of 5.
In other words, you are looking for the greatest possible difference between
two numbers in the array.

The Idea
The given array has the prices of a single stock at 13 different timestamps.
The idea is to pick two timestamps:
1. buy timestamp
2. sell timestamp
such that the buy is made before a sell. We will keep track of our max profit
while iterating over the list. At each step we will make the greedy choice by
choosing prices such that our profit is maximum.


Simplified Question:
Given the list of stock prices. Return the max profit
that can be achieved by buying the stock at the cheapest prices and selling
it at the highest price. You have to buy before selling.
Profit = Selling Price - Buying Price

Aim:
Our aim is to find the buying price and the selling price such that our
profit is maximum.

Solution:
We take min_price_index = 0 and max_price_index = 1. Now, if we find any
arr[i] that is less than our min_price, we update our min_price_index. But, if
we find an arr[i] that is greater than our max_price, to update our max_price,
we have to check whether our profit is increasing or not. If our profit is
increasing with that arr[i] > max_price, then we update the max_price.

For example, prices = [54, 18, 20, 9, 11, 999, 48, 23, 1, 7, 34, 2, 45, 67].
Here, at index = 5, min_price = 9, max_price = 999, profit = 990.
Then, at index = 8, we get our new min_price = 1. But, 67 is not our max_price
as our previous profit 990 is a better option. Thus, max_profit = 990.

Complexity Analysis:
TC: O(n)
SC: O(1)
In-place algorithm.
"""


# Solution
def max_returns(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0

    if len(arr) < 2:
        return

    for index in range(1, len(arr)):
        # current minimum price
        current_min_price = arr[current_min_price_index]

        if arr[index] < current_min_price:
            current_min_price_index = index

        # current max profit
        current_max_profit = arr[max_price_index] - arr[min_price_index]

        if current_max_profit < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index

    max_profit = arr[max_price_index] - arr[min_price_index]

    return max_profit


# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)

prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)

prices = [54, 18, 20, 9, 11, 999, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 990
test_case = [prices, solution]
test_function(test_case)
