import unittest

iters = 0

# def get_permutations(string):
#     # Generate all permutations of the input string
#     # print('length: ' + str(len(string)))
#     if len(string) <= 1:
#         return {string}
#
#     ans = []
#     for iter in range(len(string)):
#         char = string[iter]
#         smallers = get_permutations(string[0:iter] + string[iter+1:])
#         # print(smallers)
#
#         for one in smallers:
#             global iters
#             iters += 1
#             ans.append(char + one)
#
#     return set(ans)


def get_permutations(line):
    if len(line) <= 0:
        return {line}



# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        global iters
        iters = 0
        actual = get_permutations('')
        expected = {''}
        print('length: ' + str(len('')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        global iters
        iters = 0
        actual = get_permutations('a')
        expected = {'a'}
        print('length: ' + str(len('a')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        global iters
        iters = 0
        actual = get_permutations('ab')
        expected = {'ab', 'ba'}
        print('length: ' + str(len('ab')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        global iters
        iters = 0
        actual = get_permutations('abc')
        expected = {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
        print('length: ' + str(len('abc')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_three_character_string_other(self):
        global iters
        iters = 0
        actual = get_permutations('app')
        expected = {'app', 'pap', 'ppa'}
        print('length: ' + str(len('app')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_four_chars(self):
        global iters
        iters = 0
        actual = get_permutations('abcd')
        expected = {'abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                    'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                    'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                    'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'}
        print('length: ' + str(len('abcd')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

    def test_five_chars(self):
        global iters
        iters = 0
        actual = get_permutations('abcde')
        expected = {'bacde'
'ecdba'
'ebcad'
'bdeca'
'dcaeb'
'debca'
'badec'
'edacb'
'baedc'
'dabec'
'cdeab'
'aebdc'
'cbeda'
'eabdc'
'becda'
'dbeca'
'abdec'
'adbec'
'dbcae'
'aebcd'
'abecd'
'adecb'
'baced'
'deabc'
'cabde'
'eabcd'
'bdcea'
'ecdab'
'daebc'
'cdaeb'
'adcbe'
'bedca'
'cebda'
'baecd'
'cedba'
'dcbea'
'cedab'
'becad'
'aecbd'
'abced'
'bdcae'
'cadbe'
'bdaec'
'dcabe'
'beadc'
'acdeb'
'edcab'
'dcbae'
'cdbea'
'abcde'
'dbeac'
'ebdca'
'caedb'
'acdbe'
'ebdac'
'daceb'
'acebd'
'cadeb'
'aecdb'
'dbcea'
'acedb'
'acbde'
'ceadb'
'adceb'
'aedcb'
'cbead'
'dabce'
'adebc'
'ecadb'
'badce'
'cabed'
'eacbd'
'aedbc'
'ecabd'
'decab'
'dceba'
'caebd'
'dbace'
'cbade'
'edabc'
'cdbae'
'bcade'
'edcba'
'bdeac'
'cdabe'
'beacd'
'bcaed'
'adbce'
'bcdae'
'ebcda'
'bcead'
'dbaec'
'bceda'
'cbdae'
'dacbe'
'bdace'
'ceabd'
'daecb'
'decba'
'eadbc'
'edbac'
'bedac'
'edbca'
'ebadc'
'ecbda'
'bcdea'
'abedc'
'deacb'
'ecbad'
'eadcb'
'acbed'
'cbdea'
'cebad'
'dceab'
'ebacd'
'debac'
'cbaed'
'cdeba'
'abdce'
'eacdb'}
        print('length: ' + str(len('abcde')) + ', iterations: ' + str(iters))
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)