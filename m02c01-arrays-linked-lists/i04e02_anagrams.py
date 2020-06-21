"""
Exercise 2. Anagrams
The goal of this exercise is to write some code to determine if two strings
are anagrams of each other.

An anagram is a word (or phrase) that is formed by rearranging the letters of
another word (or phrase).

For example:

"rat" is an anagram of "art"
"alert" is an anagram of "alter"
"Slot machines" is an anagram of "Cash lost in me"
Your function should take two strings as input and return True if the two
words are anagrams and False if they are not.

You can assume the following about the input strings:

No punctuation
No numbers
No special characters
Note - You can use built-in methods len(), lower() and sort() on strings.

Check if the input strings are anagrams

Args:
    str1(string),str2(string): Strings to be checked if they are anagrams
Returns:
    bool: If strings are anagrams or not

Solution:
Remove the spaces from both the strings.
Sort the strings and match them with each other.

TC: O(n)
SC: O(n)
"""


def anagram_checker(str1, str2):
    # Clean strings
    clean_str_1 = str1.replace(" ", "").lower()
    clean_str_2 = str2.replace(" ", "").lower()

    if sorted(clean_str_1) == sorted(clean_str_2):
        return True

    return False


def test(str1, str2, output):
    print("Pass" if output == anagram_checker(str1, str2) else "Fail")


test('rat', 'art', True)
test('alert', 'alter', True)
test('Slot machines', 'Cash lost in me', True)
test('Dormitory', 'Dirty room', True)
test('Time and tide wait for no man', 'Notified madman into water', True)

test('water', 'waiter', False)
test('A gentleman', 'Elegant men', False)
