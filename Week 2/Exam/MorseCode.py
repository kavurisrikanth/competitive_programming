import unittest


def get_unique_transformations(words):
    for i in range(len(words)):
        words[i] = transform(words[i])

    ans = 0
    for i in range(len(words)):
        one = words[i]
        for j in range(i + 1, len(words)):
            two = words[j]
            if one == two:
                ans -= 1
                break
        ans += 1

    return ans


def transform(s):
    code = {
        'A': ".-",
        'B': "-...",
        'C': "-.-.",
        'D': "-..",
        'E': ".",
        'F': "..-.",
        'G': "--.",
        'H': "....",
        'I': "..",
        'J': ".---",
        'K': "-.-",
        'L': ".-..",
        'M': "--", 'N': "-.",
        'O': "---",
        'P': ".--.",
        'Q': "--.-",
        'R': ".-.",
        'S': "...",
        'T': "-",
        'U': "..-",
        'V': "...-",
        'W': ".--",
        'X': "-..-",
        'Y': "-.--",
        'Z': "--.."}

    ans = ''
    for c in s:
        ans += code[c.upper()]

    return ans


class Test(unittest.TestCase):
    def test_one(self):
        words = ["gin", "zen", "gig", "msg"]
        expected = 2
        self.assertEqual(get_unique_transformations(words), expected)

    def test_two(self):
        words = ["a", "z", "g", "m"]
        expected = 4
        self.assertEqual(get_unique_transformations(words), expected)

    def test_three(self):
        words = words = ["bhi", "vsv", "sgh", "vbi"]
        expected = 3
        self.assertEqual(get_unique_transformations(words), expected)

    def test_four(self):
        words = ["a", "b", "c", "d"]
        expected = 4
        self.assertEqual(get_unique_transformations(words), expected)

    def test_five(self):
        words = ["hig", "sip", "pot"]
        expected = 2
        self.assertEqual(get_unique_transformations(words), expected)


unittest.main(verbosity=2)