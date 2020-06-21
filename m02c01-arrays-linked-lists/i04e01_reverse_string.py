# Exercise 1. Reverse Strings
def string_reverser(string):
    # New empty string for us to build on
    new_string = ""

    length = len(string)
    last_index = length-1

    # Iterate over old string. Grab the charecter from the back of the string
    # and add them to the new string
    for i in range(length):
        new_string += string[last_index-i]

    # Return our solution
    return new_string


# Test
def test(function, input, output):
    print("Pass" if output == function(input) else "Fail")


input = "retaw"
output = "water"
test(string_reverser, input, output)

input = "!noitalupinam gnirts gnicitcarP"
output = "Practicing string manipulation!"
test(string_reverser, input, output)

input = "3432 :si edoc esuoh ehT"
output = "The house code is: 2343"
test(string_reverser, input, output)


# Reverse string shortcut in Python
"""
To reverse a string you can use, string[::-1]
s = 'uda city'
s[::-1] = 'ytic adu'
"""


def reverse_string(str):
    return str[::-1]


input = "retaw"
output = "water"
test(reverse_string, input, output)

input = "!noitalupinam gnirts gnicitcarP"
output = "Practicing string manipulation!"
test(reverse_string, input, output)

input = "3432 :si edoc esuoh ehT"
output = "The house code is: 2343"
test(reverse_string, input, output)
