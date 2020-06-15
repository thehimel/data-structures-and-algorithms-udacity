def sort_a_little_bit(arr, start, end):
    left_index = start
    pivot_pos = end
    pivot_value = arr[pivot_pos]

    while (pivot_pos != left_index):

        item = arr[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        arr[left_index] = arr[pivot_pos - 1]
        arr[pivot_pos - 1] = pivot_value
        arr[pivot_pos] = item
        pivot_pos -= 1

    return pivot_pos


def sort_all(arr, start, end):
    if end <= start:
        return

    pivot_pos = sort_a_little_bit(arr, start, end)
    sort_all(arr, start, pivot_pos - 1)
    sort_all(arr, pivot_pos + 1, end)


def quicksort(arr):
    sort_all(arr, 0, len(arr) - 1)


def test(arr):
    quicksort(arr)
    print(arr)


arr = [20, 35, -15, 7, 55, 1, -22]
test(arr)

arr = [8, 3, 1, 7, 0, 10, 2]
test(arr)

arr = [0]
test(arr)

arr = []
test(arr)
