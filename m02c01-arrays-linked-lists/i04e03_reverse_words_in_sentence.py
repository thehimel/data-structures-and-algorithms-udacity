"""
Exercise 3. Reverse the words in sentence
Given a sentence, reverse each word in the sentence
while keeping the order same!
"""


def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped

    Hint: to reverse a string you can use, string[::-1]
    s = 'uda city'
    s[::-1] = 'ytic adu'
    """

    word_list = our_string.split(" ")

    for word in range(len(word_list)):
        word_list[word] = word_list[word][::-1]

    return " ".join(word_list)


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
