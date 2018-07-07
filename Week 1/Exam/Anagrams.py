import unittest


def are_anagrams(one, two):
    '''
    Checks whether two strings are anagrams of each other or not.
    :param one: One string.
    :param two: The other string.
    :return: True or False
    '''

    one_letters = {}

    for char in one.lower():
        one_letters[char] = True

    for char in two.lower():
        if not 'a' <= char <= 'z':
            continue
            
        try:
            if not one_letters[char]:
                return False
        except KeyError:
            return False

    return True


class Test(unittest.TestCase):
    def test_one(self):
        one = 'anagram'
        two = 'nagaram'
        self.assertTrue(are_anagrams(one, two))

    def test_two(self):
        one = 'Keep'
        two = 'Peek'
        self.assertTrue(are_anagrams(one, two))

    def test_three(self):
        one = 'Mother In Law'
        two = 'Hitler Woman'
        self.assertTrue(are_anagrams(one, two))

    def test_four(self):
        one = 'School Master'
        two = 'The Classroom'
        self.assertTrue(are_anagrams(one, two))

    def test_five(self):
        one = 'ASTRONOMERS'
        two = 'NO MORE STARS'
        self.assertTrue(are_anagrams(one, two))

    def test_six(self):
        one = 'Toss'
        two = 'Shot'
        self.assertFalse(are_anagrams(one, two))

    def test_seven(self):
        one = 'joy'
        two = 'enjoy'
        self.assertFalse(are_anagrams(one, two))

    def test_eight(self):
        one = 'Debit Card'
        two = 'Bad Credit'
        self.assertTrue(are_anagrams(one, two))

    def test_nine(self):
        one = 'SiLeNt CAT'
        two = 'LisTen AcT'
        self.assertTrue(are_anagrams(one, two))

    def test_ten(self):
        one = 'Dormitory'
        two = 'Dirty Room'
        self.assertTrue(are_anagrams(one, two))


unittest.main(verbosity=2)