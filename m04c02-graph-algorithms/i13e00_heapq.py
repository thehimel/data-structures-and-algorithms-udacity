"""
Python's inbuilt heapq

With heapq module, you can convert a list into a min-heap.
The following two functionalities can be very handy for this task:

heappush(heap, item) — add item to the heap
heappop(heap) — remove the smallest item from the heap

Let's look at the above methods in action. We start by creating a list of int.
"""

import heapq

"""heappush"""

# initialize an empty list
min_heap = list()
heapq.heappush(min_heap, 6)
heapq.heappush(min_heap, 6)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 9)

print("After pushing, heap: {}".format(min_heap))

""" heappop """
# pop and return smallest element from the heap
smallest = heapq.heappop(min_heap)

print("Smallest element: {}".format(smallest))
print("After popping, heap: {}".format(min_heap))


"""
heappush and heappop for items with multiple entries
Note: If you insert a tuple inside the heap,
the element at 0th index of the tuple is used for comparision
"""

min_heap = list()

heapq.heappush(min_heap, (0, 1))
heapq.heappush(min_heap, (-1, 5))
heapq.heappush(min_heap, (2, 0))
heapq.heappush(min_heap, (5, -1))
heapq.heappush(min_heap, (-1, -1))

print("After pushing, heap: {}".format(min_heap))

# pop and return smallest element from the heap
smallest = heapq.heappop(min_heap)

print("Smallest element: {}".format(smallest))
print("After popping, heap: {}".format(min_heap))
