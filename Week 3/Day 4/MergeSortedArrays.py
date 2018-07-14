import unittest


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    ans = []

    one = 0
    other = 0

    while one < len(my_list) and other < len(alices_list):
        if my_list[one] <= alices_list[other]:
            ans.append(my_list[one])
            one += 1

        elif alices_list[other] < my_list[one]:
            ans.append(alices_list[other])
            other += 1

    while one < len(my_list):
        ans.append(my_list[one])
        one += 1

    while other < len(alices_list):
        ans.append(alices_list[other])
        other += 1

    return ans


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)