"""
String Key Hash Table
Problem Statement
In this quiz, you'll write your own hash table and hash function that uses
string keys. Your table will store strings in the buckets.
The (bucket) index is calculated by the first two letters of the string,
according to the formula below:
Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter

In the formula above, the generated hash value is the (bucket) index.

Example: For a string "UDACITY", the ASCII value for letters 'U' and 'D' are
85 and 68 respectively. The hash value would be: (85 *100) + 68 = 8568.

You can use the Python function ord() to get the ASCII value of a letter,
and chr() to get the letter associated with an ASCII value.


Assumptions
The string will have at least two letters,
The first two characters are uppercase letters (ASCII values from 65 to 90).

Rules
Do not use a Python dictionary—only lists!
Store lists at each bucket, and not just the string itself.
For example, you can store "UDACITY" at index 8568 as ["UDACITY"].

Instructions
Create a HashTable class, with the following functions:
store() - a function that takes a string as input,
    and stores it into the hash table.
lookup() - a function that checks if a string is already available
    in the hash table. If yes, return the hash value, else return -1.
calculate_hash_value() - a helper function to calculate a hash value
    of a given string.
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    # Input a string that has to be stored in the table.
    def store(self, string):
        hv = self.calculate_hash_value(string)   # generate the hash value

        if hv != -1:  # if the string is a new one
            if self.table[hv] is not None:  # if the bucket is non-empty
                self.table[hv].append(string)  # append the string in the list at that bucket
            else:
                self.table[hv] = [string]  # store the string in a new list at that bucket

    # Return the hash value if the string is already in the table.
    # Return -1 otherwise.
    def lookup(self, string):
        hv = self.calculate_hash_value(string)

        # Check collision, and confirm the availability of the given string
        # There might be a case when two strings can generate same hash value.
        # However, one string is present, and other one is not.
        if self.table[hv] is not None:
            if string in self.table[hv]:
                return hv

        return -1  # otherwise

    # Helper function to calulate a hash value from a string.
    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value


# TESTING Setup
hash_table = HashTable()

# Test calculate_hash_value
print(hash_table.calculate_hash_value('UDACITY'))  # Should be 8568

# Test lookup edge case
print(hash_table.lookup('UDACITY'))  # Should be -1

# Test store
hash_table.store('UDACITY')
print(hash_table.lookup('UDACITY'))  # Should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))  # Should be 8568
