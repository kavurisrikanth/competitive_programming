import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    # Check if the shuffled deck is a single riffle of the halves
    i = j = 0
    for card in shuffled_deck:
        if i < len(half1) and j < len(half2):
            if half1[i] != card and half2[j] != card:
                return False

            if half1[i] == card:
                i += 1
            elif half2[j] == card:
                j += 1

        elif i < len(half1):
            if half1[i] != card:
                return False
            i += 1

        elif j < len(half2):
            if half2[j] != card:
                return False
            j += 1

        else:
            return False

    return True


# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)