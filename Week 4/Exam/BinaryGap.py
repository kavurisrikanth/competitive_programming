import unittest


def get_binary_gap(n):
    ans = 0
    temp = 0
    started = False

    while n > 0:
        x = n % 2
        if x == 1:
            if not started:
                started = True
            temp += 1
        else:
            if started:
                started = False
            ans = max(ans, temp)
            temp = 0
        n //= 2

    ans = max(ans, temp)
    return ans if ans > 1 else 0


class Test(unittest.TestCase):
    def test_one(self):
        n = 22
        exp = 2
        act = get_binary_gap(n)
        self.assertEqual(exp, act)


unittest.main(verbosity=2)