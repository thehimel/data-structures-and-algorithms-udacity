class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


stack = Stack()

stack.push("Web Page 1")
stack.push("Web Page 2")
stack.push("Web Page 3")

print(stack.items)

stack.pop()
stack.pop()

print("Pass" if (stack.items[0] == 'Web Page 1') else "Fail")

stack.pop()

print("Pass" if (stack.pop() is None) else "Fail")
