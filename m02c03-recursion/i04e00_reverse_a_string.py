
"""
RECURSIVE FUNCTION
Args: input(str): string to be reversed
Returns: a string that us reversed of input
"""
"""
The `slice()` function can accept upto the following three arguments.
- start: [OPTIONAL] starting index. Default value is 0.
- stop: ending index (exclusive)
- step_size: [OPTIONAL] the increment size. Default value is 1.

The return type of `slice()` function is an object of class 'slice'.
"""

"""
Solution logic:
With every call we keeping the present element to the last.
Input = 'abcd'
reverse_string('abcd')
    reverse_string('bcd') + 'a'
        reverse_string('cd') + 'b' + 'a'
            reverse_string('d') + 'c' + 'b' + 'a'
                return 'd' + 'c' + 'b' + 'a'
Output: dcba
"""


# Solution
def reverse_string(input):

    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        return reverse_string(input[1:]) + input[0]


"""
**Time and Space Complexity Analysis**
Looking at this, you might think it has a running time of O(n), but that isn't
correct due to the slice operation array[1:]. This operation will take O(k)
time to run where k is the number of elements to copy. So, this function is
actually O(k∗n) running time complexity and O(k∗n) space complexity.

Each recursive call to the `reverse_string()` function will create
a new set of local variables - first_char, the_rest, sub_string,
and reversed_substring. Therefore, the space complexity of a recursive function
would always be proportional to the maximum depth of recursion stack.

The time complexity for this function will be  O(k*n), where k is a constant
and n is the number of characters in the string (depth of recursion stack).
"""

# Test
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print("Pass" if ("dcba" == reverse_string("abcd")) else "Fail")
