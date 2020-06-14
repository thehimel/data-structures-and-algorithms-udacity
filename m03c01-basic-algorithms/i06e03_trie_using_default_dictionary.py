"""
Trie is with a Python default dictionary. The following TrieNod class is using
collections.defaultdict instead of a normal dictionary.

The children inside the TrieNode here is by default having all the characters.
"""

import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # Add `word` to trie
    def add(self, word):
        node = self.root

        for char in word:
            node = node.children[char]

        node.is_word = True

    # Check if word exists in trie
    def exists(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_word

    # Return all items in the Trie
    def get_items(self):
        node = self.root
        output = list()
        return self.get_items_recursive(node, output)

    def get_items_recursive(self, node, output):
        if len(node.children) == 0:
            return

        output += list(node.children.keys())
        for char in node.children:
            self.get_items_recursive(node.children[char], output)

        return output


# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('t')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')

print('All tests passed!')

print(word_trie.get_items())
