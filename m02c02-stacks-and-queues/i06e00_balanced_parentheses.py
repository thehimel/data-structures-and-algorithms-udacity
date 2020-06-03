"""
Balanced Parentheses Exercise
In this exercise you are going to apply what you learned about stacks
with a real world problem. We will be using stacks to make sure
the parentheses are balanced in mathematical expressions such as:
((32+8)∗(5/2))/(2+6).  In real life you can see this extend to many things
such as text editor plugins and interactive development environments for
all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses
are balanced or False if it is not.

Try to code up a solution and pass the test cases.
"""


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


"""
Check equation for balanced parentheses

Args:
    equation(string): String form of equation
Returns:
    bool: Return if parentheses are balanced or not

Solution:
Whenever you get the start paranthesis, push it in the stack.
Wenver you get the end paranthesis, pop it from the stack.
If nothing is popped, return False.

At the end, if there is nothing in the stack, return True.
Else, return False.
"""


def equation_checker(equation):
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if not stack.pop():
                return False

    if stack.size() == 0:
        return True
    else:
        return False


# Test
print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
