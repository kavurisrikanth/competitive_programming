import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time
    ans = [0] * len(unsorted_scores)
    counts = [0] * (highest_possible_score + 1)

    # count frequencies of numbers
    for num in unsorted_scores:
        counts[num] += 1

    # print('after counting')
    # print(counts)

    # get starting indices
    start_index = 0
    for num in range(len(counts) - 1, -1, -1):
        old_count = counts[num]
        counts[num] = start_index
        start_index += old_count

    # print('after getting starting indices')
    # print(counts)

    for num in unsorted_scores:
        ans[counts[num]] = num
        counts[num] += 1

    return ans


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)