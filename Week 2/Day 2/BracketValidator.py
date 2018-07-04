import unittest


def is_valid(code):
    # Determine if the input code is valid
    stack = []

    for char in code:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char == ')' or char == '}' or char == ']':

            try:
                last_open = stack[-1]
                if (char == ')' and last_open != '(') or \
                        (char == '}' and last_open != '{') or \
                    (char == '[' and last_open != ']'):
                    return False

                stack.pop()
            except IndexError:
                return False

    return len(stack) == 0


# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)