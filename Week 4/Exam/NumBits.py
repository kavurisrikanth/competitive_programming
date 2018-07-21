import unittest

def get_num_ones(n):
    ans = 0
    while n > 0:
        x=  n % 2
        if x == 1:
            ans += 1
        n //= 2
    return ans


def get_num_ones_range(n):
    ans = []
    for i in range(n+1):
        ans.append(get_num_ones(i))
    return ans


class Test(unittest.TestCase):
    def test_one(self):
        n = 15
        exp = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        self.assertEqual(get_num_ones_range(n), exp)

    def test_two(self):
        n = 16
        exp = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]
        self.assertEqual(get_num_ones_range(n), exp)

    def test_three(self):
        n = 1
        exp = [0, 1]
        self.assertEqual(get_num_ones_range(n), exp)

    def test_four(self):
        n = 25
        exp = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3]
        self.assertEqual(get_num_ones_range(n), exp)

    def test_five(self):
        n = 5
        exp = [0, 1, 1, 2, 1, 2]
        self.assertEqual(get_num_ones_range(n), exp)

    def test_six(self):
        n = 6
        exp = [0, 1, 1, 2, 1, 2, 2]
        self.assertEqual(get_num_ones_range(n), exp)




unittest.main(verbosity=2)