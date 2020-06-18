# Helper code
import collections

# An item can be represented as a namedtuple
Item = collections.namedtuple('Item', ['weight', 'value'])


# DP Solution
# Get the max total value ($) of items that can be placed into the knapsack
def knapsack_max_value(knapsack_max_weight, items):

    # Initialize a lookup table to store the maximum value ($)
    lookup_table = [0] * (knapsack_max_weight + 1)

    # Iterate down the given list
    for item in items:
        # The "capcacity" represents amount of remaining capacity (kg)
        # of knapsack at a given moment.
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(
                    lookup_table[capacity],
                    lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


# Test
tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [
                    Item(10, 2), Item(29, 10), Item(5, 7),
                    Item(5, 3), Item(5, 1), Item(24, 12)]}}]


for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
