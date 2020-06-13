"""
Complexity:
At every step, the input size is being half.
TC: O(log(n))
SC: O(1)
"""


# Recursive solution
def search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end)//2
    mid_element = array[mid]

    if mid_element == target:
        return mid

    elif target < mid_element:
        end = mid - 1
        return search(array, target, start, end)

    else:
        start = mid + 1
        return search(array, target, start, end)


def recursive_binary_search(array, target):
    start = 0
    end = len(array) - 1
    return search(array, target, start, end)


def test_function(test_case):
    answer = recursive_binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 100
index = -1
test_case = [array, target, index]
test_function(test_case)
