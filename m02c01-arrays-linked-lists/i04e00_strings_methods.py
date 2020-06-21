# Common String Methods
# Ref: https://docs.python.org/3/library/stdtypes.html#string-methods

str1 = "Udacity"


# LENGTH
print(len(str1))		# 7


# CHANGE CASE
# The `lower()` and `upper` method returns the string in lower case
# and upper case respectively
print(str1.lower())		# udacity
print(str1.upper())		# UDACITY


# SLICING
# string_var[lower_index : upper_index]
# Note that the upper_index is not inclusive.
print(str1[1:6]) 		# dacit
print(str1[:6])			# Udacit. A blank index means "all from that end"
print(str1[1:])			# dacity

# A negative index means start slicing from the end-of-string
print(str1[-6:-1])		# dacit


# STRIP
# `strip()` removes any whitespace from the beginning or the end
str2 = "    Udacity    "
print(str2.strip())		# Udacity


# REPLACE/SUBSTITUTE A CHARACTER IN THE STRING
# The replace() method replaces all occurances a character in a string
# with another character. The input arguments are case-sensitive
print(str1.replace('y', "B"))  # UdacitB


# SPLIT INTO SUB-STRINGS
# The split() method splits a string into substrings based on the separator
# that we specify as argument
str3 = "Welcome, Constance!"
print(str3.split(","))  # ['Welcome', ' Constance!']


# CONCATENATION
print(str3 + " " + str1)  # Welcome, Constance! Udacity
marks = 100
# print(str3 + " You have scored a perfect " + marks)
# TypeError: can only concatenate str (not "int") to str


# format() method converts the argument as a formatted string
print(str3 + " You have scored a perfect " + format(marks))


# SORT A STRING
# We can use sorted() method that sort any instance of *iterable*.
# The characters are compared based on their ascii value
# [' ', '!', ',', 'C', 'W', 'a', 'c', 'c', 'e', 'e', 'e',
#   'l', 'm', 'n', 'n', 'o', 'o', 's', 't']
print(sorted(str3))
