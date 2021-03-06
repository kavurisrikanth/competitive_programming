import unittest


def generate_parenthesis_permutations(n):
    ans = []
    get_parens(n * 2, ans)
    return ans


def get_parens(n, arr):
    get_parens_recursive(n//2, n//2, '', arr)


def get_parens_recursive(open, close, line, arr):
    # print(arr)
    # print('line: ' + line)

    if open == 0 and close == 0:
        arr.append(line)
        # print(arr)
        return

    if open > close:
        return

    if open > 0:
        get_parens_recursive(open - 1, close, line + '(', arr)

    if close > 0:
        get_parens_recursive(open, close - 1, line + ')', arr)


class Test(unittest.TestCase):
    def test_one(self):
        n = 2
        expected = [ '(())',   '()()' ]
        actual = generate_parenthesis_permutations(n)
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected))

    def test_two(self):
        n = 3
        expected = ['((()))', '(()())', '(())()', '()(())', '()()()']
        actual = generate_parenthesis_permutations(n)
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected))

    def test_three(self):
        n = 5
        expected = ['((((()))))', '(((()())))', '(((())()))', '(((()))())', '(((())))()', '((()(())))',
                    '((()()()))', '((()())())', '((()()))()', '((())(()))', '((())()())', '((())())()',
                    '((()))(())', '((()))()()', '(()((())))', '(()(()()))', '(()(())())', '(()(()))()',
                    '(()()(()))', '(()()()())', '(()()())()', '(()())(())', '(()())()()', '(())((()))',
                    '(())(()())', '(())(())()', '(())()(())', '(())()()()', '()(((())))', '()((()()))',
                    '()((())())', '()((()))()', '()(()(()))', '()(()()())', '()(()())()', '()(())(())',
                    '()(())()()', '()()((()))', '()()(()())', '()()(())()', '()()()(())', '()()()()()' ]
        actual = generate_parenthesis_permutations(n)
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected))

    def test_four(self):
        n = 4
        expected = [ '(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()',
                     '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
        actual = generate_parenthesis_permutations(n)
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected))

    def test_five(self):
        n = 6
        expected = [ '(((((())))))', '((((()()))))', '((((())())))', '((((()))()))', '((((())))())',
                     '((((()))))()', '(((()(()))))', '(((()()())))', '(((()())()))', '(((()()))())',
                     '(((()())))()', '(((())(())))', '(((())()()))', '(((())())())', '(((())()))()',
                     '(((()))(()))', '(((()))()())', '(((()))())()', '(((())))(())', '(((())))()()',
                     '((()((()))))', '((()(()())))', '((()(())()))', '((()(()))())', '((()(())))()',
                     '((()()(())))', '((()()()()))', '((()()())())', '((()()()))()', '((()())(()))',
                     '((()())()())', '((()())())()', '((()()))(())', '((()()))()()', '((())((())))',
                     '((())(()()))', '((())(())())', '((())(()))()', '((())()(()))', '((())()()())',
                     '((())()())()', '((())())(())', '((())())()()', '((()))((()))', '((()))(()())',
                     '((()))(())()', '((()))()(())', '((()))()()()', '(()(((()))))', '(()((()())))',
                     '(()((())()))', '(()((()))())', '(()((())))()', '(()(()(())))', '(()(()()()))',
                     '(()(()())())', '(()(()()))()', '(()(())(()))', '(()(())()())', '(()(())())()',
                     '(()(()))(())', '(()(()))()()', '(()()((())))', '(()()(()()))', '(()()(())())',
                     '(()()(()))()', '(()()()(()))', '(()()()()())', '(()()()())()', '(()()())(())',
                     '(()()())()()', '(()())((()))', '(()())(()())', '(()())(())()', '(()())()(())',
                     '(()())()()()', '(())(((())))', '(())((()()))', '(())((())())', '(())((()))()',
                     '(())(()(()))', '(())(()()())', '(())(()())()', '(())(())(())', '(())(())()()',
                     '(())()((()))', '(())()(()())', '(())()(())()', '(())()()(())', '(())()()()()',
                     '()((((()))))', '()(((()())))', '()(((())()))', '()(((()))())', '()(((())))()',
                     '()((()(())))', '()((()()()))', '()((()())())', '()((()()))()', '()((())(()))',
                     '()((())()())', '()((())())()', '()((()))(())', '()((()))()()', '()(()((())))',
                     '()(()(()()))', '()(()(())())', '()(()(()))()', '()(()()(()))', '()(()()()())',
                     '()(()()())()', '()(()())(())', '()(()())()()', '()(())((()))', '()(())(()())',
                     '()(())(())()', '()(())()(())', '()(())()()()', '()()(((())))', '()()((()()))',
                     '()()((())())', '()()((()))()', '()()(()(()))', '()()(()()())', '()()(()())()',
                     '()()(())(())', '()()(())()()', '()()()((()))', '()()()(()())', '()()()(())()',
                     '()()()()(())', '()()()()()()' ]
        actual = generate_parenthesis_permutations(n)
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), len(expected))


unittest.main(verbosity=2)