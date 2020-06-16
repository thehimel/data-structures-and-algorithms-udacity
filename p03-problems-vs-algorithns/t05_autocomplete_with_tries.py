"""
Task 5: Autocomplete with Trie - Finding Suffixes
Suppose, we have a functioning Trie, we need to add the ability
to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the TrieNode object
that will return all complete word suffixes that exist below it in the trie.
For example, if our Trie contains the words ["fun", "function", "factory"]
and we ask for suffixes from the f node, we would expect to receive
["un", "unction", "actory"] back from node.suffixes().

Hint: recurse down the trie, collecting suffixes as you go.

Solution:
Get the node representing the prefix.
Return all suffixes of that node found with recursive operation.

Complexity Analysis:
TC: O(k)
SC: O(k)
m = suffixes found from the prefix.
n = total number of suffixes.
k = total length of all suffixes
k = len(prefix) + (len(m1) + len(m2) + len(m3) + ......... len(mn))
"""


class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    # Recursive function that collects the suffix for all complete words
    # below this point
    def suffixes(self, suffix=''):

        suffixes = []

        # Traverse through the children
        for char, node in self.children.items():

            # If the node specifies the end of a word
            if node.is_word:
                suffixes.append(suffix + char)

            # If the node contains more children
            # Add those children to the current suffixes recursively
            if node.children:
                suffixes.extend(node.suffixes(suffix + char))

        return suffixes


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # Add `word` to trie
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.insert(char)
            node = node.children[char]

        node.is_word = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):
        node = self.root

        # Traverse through the characters in the prefix
        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        # Return the node that represents this prefix
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def test(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


test('ant')
test('f')
test('fu')
