basic_trie = {
    # words: a, add
    'a': {
        'word_end': True,
        'd': {
            'word_end': False,
            'd': {
                'word_end': True
            }
        }
    },
    # words: hi
    'h': {
        'word_end': False,
        'i': {
            'word_end': True
        }
    }
}


# Look for the word in `basic_trie`
def is_word(word):
    node = basic_trie

    for char in word:
        if char not in node:
            return False

        node = node[char]

    return node['word_end']


# Test words
test_words = ['ap', 'add', 'hi']
for word in test_words:
    if is_word(word):
        print(f'"{word}" is a word.')
    else:
        print(f'"{word}" is not a word.')
