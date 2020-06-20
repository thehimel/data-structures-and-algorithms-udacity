"""
Task 3: Rearrange Array Digits

Rearrange Array Elements so as to form two number such that their
sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9].
The number of digits in both numbers cannot differ by more than 1.
You're not allowed to use any sorting function that Python provides
and the expected time complexity is O(nlog(n)).

For example, [1, 2, 3, 4, 5]
The expected answer would be [531, 42].
Another expected answer can be [542, 31].
If there are more than one possible answers, return anyone.

Args: input_list(list): Input List
Returns: (int), (int): Two maximum sums

Solution:
---------
We know that, largest number can be found from digits (0-9) when they are
placed from larger to smaller form. That means formed in descending order.

Sort the array with merge sort from larger to smaller. Construct 2 numbers.
First with the odd indices of the sorted array. Second with the even indices
of the sorted array. Return these 2 numbers in a list.

Example:
Input: [1, 2, 3, 4, 5]
Sorted array from max to min numbers: [5, 4, 3, 2, 1]
x = 531
y = 42
Output: [531, 42]

Complexity Analysis:
TC: T(merge_sort) + O(n) => O(nlog(n)) + O(n) => O(nlog(n))
SC: T(merge_sort) + O(n) => O(n) + O(n) => O(n)

TC: O(nlog(n))
SC: O(n)
"""


def split(arr, start, end):
    if(start < end):
        mid = (start + end) // 2
        split(arr, start, mid)
        split(arr, mid+1, end)

        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    p = start
    q = mid + 1
    temp_arr = [None for _ in range(end+1 - start)]
    k = 0

    for i in range(start, end+1):
        if (p > mid):
            temp_arr[k] = arr[q]
            k += 1
            q += 1

        elif (q > end):
            temp_arr[k] = arr[p]
            k += 1
            p += 1

        # Adding the larger value
        elif (arr[p] > arr[q]):
            temp_arr[k] = arr[p]
            k += 1
            p += 1
        else:
            temp_arr[k] = arr[q]
            k += 1
            q += 1

    k = 0
    while(k < len(temp_arr)):
        arr[start] = temp_arr[k]
        start += 1
        k += 1


def mergesort(arr):
    split(arr, 0, len(arr) - 1)
    return arr


# Main Solution
def rearrange_digits(arr):
    # sort the array in descending order: larger to smaller number.
    arr = mergesort(arr)

    # Create x with digits at the odd indices of sorted array
    x = 0
    for i in range(0, len(arr), 2):
        x = x * 10 + arr[i]

    # Create y with digits at the even indices of sorted array
    y = 0
    for i in range(1, len(arr), 2):
        y = y * 10 + arr[i]

    return [x, y]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test edge cases
test_function([[], []])
test_function([[0], [0, 0]])
test_function([[-1], [-1, 0]])

# General tests
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
