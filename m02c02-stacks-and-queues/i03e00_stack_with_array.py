class Stack:
    def __init__(self, arr_size=10):
        self.arr = self._create_arr(arr_size)
        self.top = 0
        self.num_elements = 0

    def push(self, data):
        if self.top == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._increase_stack_capacity()

        self.arr[self.top] = data
        self.top += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            self.top = 0
            return None
        self.top -= 1
        self.num_elements -= 1
        return self.arr[self.top]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _create_arr(self, arr_size):
        return [None for _ in range(arr_size)]

    def _increase_stack_capacity(self):
        self.arr += self._create_arr(2 * len(self.arr))


# Test

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)

# The array is now at capacity!
# This one should cause the array to increase in size
stack.push(11)

# Using a variable for the last_item just to check the pop() method
last_item = 12
stack.push(last_item)

print(stack.arr)  # Let's see what the array looks like now!

# If we successfully increased the array size.
print("Pass" if len(stack.arr) > 10 else "Fail")
print("Pass" if stack.pop() == last_item else "Fail")
