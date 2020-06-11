"""
Write code for finding all files under a directory
and all directories beneath it that end with ".c"

Find all files beneath path with file name suffix.

Note that a path may contain further subdirectories
and those subdirectories may also contain further subdirectories.

There are no limit to the depth of the subdirectories can be.

Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

Returns:
    a list of paths


Python's os module will be useful—in particular, you can use:
os.path.isdir(path)
os.path.isfile(path)
os.listdir(directory)
os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task
very easily. However, for this problem you are not allowed to use os.walk().
"""

import os


def find_files(suffix, path):
    return None


#  Let us print the files in the directory in which you are running this script
print(os.listdir("."))

#  Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

#  Does the file end with .py?
print("./ex.py".endswith(".py"))
