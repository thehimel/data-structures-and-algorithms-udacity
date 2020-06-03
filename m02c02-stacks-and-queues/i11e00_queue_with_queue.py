class Queue:
    def __init__(self, initial_size=10):
        self.arr = self._create_arr(initial_size)
        self.rear = 0

    def enqueue(self, data):
        if self.rear == len(self.arr):
            self._increase_capacity()

        self.arr[self.rear] = data
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            return None

        data = self.arr[0]
        # Keep values from index 1 to last of the present arr
        # and add one item at last
        self.arr = self.arr[1:] + self._create_arr(1)
        self.rear -= 1
        return data

    def size(self):
        return self.rear

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.arr[0]

    def _create_arr(self, arr_size):
        return [None for _ in range(arr_size)]

    def _increase_capacity(self):
        self.arr += self._create_arr(2 * len(self.arr))


# Test
# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")
