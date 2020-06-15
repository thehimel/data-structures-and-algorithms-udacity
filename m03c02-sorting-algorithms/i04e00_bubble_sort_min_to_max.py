"""
First for loop runs from 0 to n-1
Second iteration runs from 1 to n-1 - i, where i = iteration of first for loop

After the first round, we know that the max value is placed at the last index,
thus we don't need to consider the last index on the next round.
Then, on the next round, the 2nd last index, contains the 2nd last max value.
"""


def bubble_sort_min(arr):
    for iteration in range(len(arr)):
        for index in range(1, len(arr) - iteration):
            this = arr[index]
            prev = arr[index - 1]

            if prev <= this:
                continue

            arr[index] = prev
            arr[index - 1] = this
        # print(arr)


arr = [
    16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]

bubble_sort_min(arr)
print("Pass" if (arr[0] == 3) else "Fail")
