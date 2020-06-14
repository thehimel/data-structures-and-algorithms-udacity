class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # Add `word` to trie
    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
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


word_list = [
    'apple', 'bear', 'goo', 'good', 'goodbye',
    'goods', 'goodwill', 'gooses', 'zebra']

word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print(f'"{word}" is a word.')
    else:
        print(f'"{word}" is not a word.')


print(word_trie.get_items())
