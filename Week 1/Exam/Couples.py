import unittest

def handy_hold(couples):
    aux = [-1] * (max(couples) + 1)

    for i in range(len(couples)):
        aux[couples[i]] = i

    swaps = 0

    for i in range(len(couples) - 1):
        # print('i: ' + str(i))
        one = couples[i]
        left = couples[i - 1] if i != 0 else None
        right = couples[i + 1] if i != len(couples) - 1 else None

        if in_correct_place(one, left, right):
            continue

        # print(left)
        # print(one)
        # print(right)

        other = get_other(one)
        other_index = aux[other]
        couples[i + 1], couples[other_index] = couples[other_index], couples[i + 1]
        swaps += 1

    return swaps


def get_other(num):
    return num + 1 if num % 2 == 0 else num - 1


def in_correct_place(num, left=None, right=None):
    other = get_other(num)
    # print(num)
    # print(other)
    # print(right)

    if left and right:
        return left == other or right == other

    if left:
        return other == left

    if right:
        return other == right


class Test(unittest.TestCase):
    # def test_one(self):
    #     couples = [1,3,4,0,2,5]
    #     expected = 2
    #     self.assertEqual(handy_hold(couples), expected)
    #
    # def test_two(self):
    #     couples = [3,2,0,1]
    #     expected = 0
    #     self.assertEqual(handy_hold(couples), expected)

    # def test_three(self):
    #     couples =  [3,30,50,90,16,91,65,18,61,58]
    #     expected = 5
    #     self.assertEquals(handy_hold(couples), expected)
    #
    # def test_four(self):
    #     couples = [3,1,5,4,6,2]
    #     expected = 2
    #     self.assertEquals(handy_hold(couples), expected)
    #
    # def test_five(self):
    #     couples = [55,37,19,46,66,32,7,81,33,76,00,28,92,26,99,6,56,29,17,52,90,79,91,83,12,40,82,84,2,21,11,68,98,34,73,10,57,58,64,36]
    #     expected = 20
    #     self.assertEquals(handy_hold(couples), expected)

    def test_six(self):
        couples = [1, 0]
        expected = 0
        self.assertEqual(handy_hold(couples), expected)

    # def test_seven(self):
    #     couples =  [50,23,76,19,16,70,35,68,41,49,99,71,59,95,89,33,22,7,54,83,24,0,18,64,11,14,77,26,42,21,82,1,97,52,65,79,37,62,60,91,98,4,88,36,51,20,85,90,29,84,93,13,80,6,55,48,2,40,46,81,30,3,94,38,27,31,53,86,32,96,8,58,73,5]
    #     expected = 37
    #     self.assertEquals(handy_hold(couples), expected)


unittest.main(verbosity=2)