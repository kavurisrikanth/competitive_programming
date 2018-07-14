import unittest

def get_hamming_distance(x, y):
    ans = 0
    while x > 0 and y > 0:
        x_digit = x % 2
        y_digit = y % 2

        if x_digit != y_digit:
            ans += 1

        x = x // 2
        y = y // 2

    while x > 0:
        x_digit = x % 2
        if x_digit == 1:
            ans += 1

        x = x // 2

    while y > 0:
        y_digit = y % 2
        if y_digit == 1:
            ans += 1

        y = y // 2

    return ans

class Test(unittest.TestCase):

    def test_one(self):
        x = 25
        y = 30
        expected = 3
        self.assertEqual(get_hamming_distance(x, y), expected)

    def test_two(self):
        x = 1
        y = 4
        expected = 2
        self.assertEqual(get_hamming_distance(x, y), expected)


    def test_three(self):
        x = 25
        y = 30
        expected = 3
        self.assertEqual(get_hamming_distance(x, y), expected)

    def test_four(self):
        x = 100
        y = 250
        expected = 5
        self.assertEqual(get_hamming_distance(x, y), expected)

    def test_five(self):
        x = 1
        y = 30
        expected = 5
        self.assertEqual(get_hamming_distance(x, y), expected)

    def test_six(self):
        x = 0
        y = 255
        expected = 8
        self.assertEqual(get_hamming_distance(x, y), expected)


unittest.main(verbosity=2)