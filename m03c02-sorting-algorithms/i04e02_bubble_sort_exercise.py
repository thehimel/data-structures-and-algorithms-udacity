"""
Sam doesn't always go to sleep in the same hour. Given the following times
Sam has gone to sleep, sort the times from latest to earliest.
"""


def bubble_sort(arr):
    for iteration in range(len(arr)):
        for index in range(1, len(arr) - iteration):
            this_hour, this_min = arr[index]
            prev_hour, prev_min = arr[index - 1]

            if prev_hour > this_hour or (
                    prev_hour == this_hour and prev_min >= this_min):
                continue

            arr[index] = (prev_hour, prev_min)
            arr[index - 1] = (this_hour, this_min)


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [
    (24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]

bubble_sort(sleep_times)
print("Pass" if sleep_times[0] == (24, 23) else "Fail")
