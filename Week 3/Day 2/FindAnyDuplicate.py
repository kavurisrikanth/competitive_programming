import unittest


# def find_repeat(the_list):
#     # Find a number that appears more than once
#     for i in range(len(the_list)):
#         for j in range(i + 1, len(the_list)):
#             if the_list[i] == the_list[j]:
#                 return the_list[j]
#
#     return 0


def find_repeat(arr):
    start = 1
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start)//2
        low_start, low_end = start, mid
        high_start, high_end = mid + 1, end

        actual_num = 0
        expected_num = low_end - low_start + 1
        for item in arr:
            if low_start <= item <= low_end:
                actual_num += 1

        if actual_num > expected_num:
            start, end = low_start, low_end
        else:
            start, end = high_start, high_end

    return start


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)