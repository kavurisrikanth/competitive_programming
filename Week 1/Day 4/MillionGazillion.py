import unittest


class Trie(object):

    def __init__(self):
        self.root = {}
    # Implement a trie and use it to efficiently store strings

    def add_word(self, word):
        current = self.root
        new_word = False

        for letter in word:
            if letter not in current:
                new_word = True
                current[letter] = {}
            current = current[letter]

        if "\0" not in current:
            new_word = True
            current["\0"] = {}

        return new_word


# Tests

class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.add_word('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.add_word('cakes')
        self.assertTrue(result, msg = 'new word 2')

        result = trie.add_word('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.add_word('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.add_word('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.add_word('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.add_word('')
        self.assertTrue(result, msg='empty word')

        result = trie.add_word('')
        self.assertFalse(result, msg='empty word present')


unittest.main(verbosity=2)