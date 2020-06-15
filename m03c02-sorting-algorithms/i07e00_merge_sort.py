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

        elif (arr[p] < arr[q]):
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


if __name__ == '__main__':
    arr = [20, 35, -15, 7, 55, 1, -22]
    split(arr, 0, len(arr) - 1)
    print(arr)
