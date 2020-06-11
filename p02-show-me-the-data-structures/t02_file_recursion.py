"""
File Recursion

Problem Statement
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


Solution:
List the files in the present directory.
If an entry ends with the given suffix, add it to the output list.
If an entry is directory, call the function recursively
to get files in that directory.

Complexity Analysis:
n = total number of files/directories in the given path.

TC: O(n)
SC: O(n)
"""

import os


def find_files(suffix, path):
    # create a list of file and sub directories
    # names in the given directory
    file_list = os.listdir(path)
    all_files = list()
    # Iterate over all the entries
    for entry in file_list:
        # Create full path
        full_path = os.path.join(path, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + find_files(suffix, full_path)
        else:
            if full_path.endswith(suffix):
                all_files.append(full_path)

    return all_files


suffix = '.c'
path = '.'

# Get the list of all files in directory tree at given path
output = find_files(suffix, path)
print(output)
