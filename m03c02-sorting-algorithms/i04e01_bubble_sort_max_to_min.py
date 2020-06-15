def bubble_sort_max(arr):
    for iteration in range(len(arr)):
        for index in range(1, len(arr) - iteration):
            this = arr[index]
            prev = arr[index - 1]

            if prev >= this:
                continue

            arr[index] = prev
            arr[index - 1] = this
        # print(arr)


arr = [
    16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]

bubble_sort_max(arr)
print("Pass" if (arr[0] == 56) else "Fail")
