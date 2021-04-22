"""
Exercise 3. Reverse the words in sentence
Given a sentence, reverse each word in the sentence
while keeping the order same!

Flip the individual words in a sentence

Args:
    our_string(string): Strings to have individual words flip
Returns:
    string: String with words flipped

Hint: to reverse a string you can use, string[::-1]
s = 'uda city'
s[::-1] = 'ytic adu'
"""


def word_flipper(our_string):
    word_list = our_string.split(" ")

    for i, word in enumerate(word_list):
        word_list[i] = word[::-1]

    return " ".join(word_list)


# Test
def test(function, input, output):
    print("Pass" if output == function(input) else "Fail")


test(word_flipper, "retaw", "water")
test(word_flipper, "sihT si na elpmaxe", "This is an example")

test(
    word_flipper,
    "sihT si eno llams pets rof ...",
    "This is one small step for ...")
