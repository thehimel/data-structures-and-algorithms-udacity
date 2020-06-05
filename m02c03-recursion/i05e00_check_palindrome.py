"""
A palindrome is a word that is the reverse of itself—that is,
it is the sameword when read forwards and backwards.

For example:

"madam" is a palindrome
"abba" is a palindrome
"cat" is not
"a" is a trivial case of a palindrome
"""

"""
Return True if input is palindrome, False otherwise.

Args:
    input(str): input to be checked if it is palindrome
"""

# Note: After the last element the index will be -1,
#   thus the condition is if len(input) <= 1


def is_palindrome(input):
    # Termination / Base condition
    if len(input) <= 1:
        return True
    else:
        first_char = input[0]
        last_char = input[-1]

        # sub_input is input with first and last char removed
        sub_input = input[1:-1]

        # recursive call, if first and last char are identical,
        #   else return False
        return (first_char == last_char) and is_palindrome(sub_input)


# Logic is same as is_palindrome(), but solved in less lines of code
def is_palindrome2(input):
    if len(input) <= 1:
        return True
    else:
        return (input[0] == input[-1]) and is_palindrome(input[1:-1])


# Test
print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")

print("Pass" if (is_palindrome2("")) else "Fail")
print("Pass" if (is_palindrome2("a")) else "Fail")
print("Pass" if (is_palindrome2("madam")) else "Fail")
print("Pass" if (is_palindrome2("abba")) else "Fail")
print("Pass" if not (is_palindrome2("Udacity")) else "Fail")
