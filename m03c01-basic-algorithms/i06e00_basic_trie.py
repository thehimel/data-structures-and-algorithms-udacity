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

print('Is "a"   a word: {}'.format(basic_trie['a']['word_end']))
print('Is "ad"  a word: {}'.format(basic_trie['a']['d']['word_end']))
print('Is "add" a word: {}'.format(basic_trie['a']['d']['d']['word_end']))
print('Is "h"   a word: {}'.format(basic_trie['h']['word_end']))
print('Is "hi"  a word: {}'.format(basic_trie['h']['i']['word_end']))
