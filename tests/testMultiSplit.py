import unittest
from main import multisplit 


class TestSplit(unittest.TestCase):
    def test_empty_delims(self):
        self.assertEqual(multisplit('abc', []), ['abc'])
        with self.assertRaises(ValueError):
            multisplit('abc', [''])
        with self.assertRaises(ValueError):
            multisplit('abc', ['', 'a'])
    def test_splits(self):
        self.assertEqual(multisplit('', ['a']), [])
        self.assertEqual(multisplit('a', ['a']), [])
        self.assertEqual(multisplit('ab', ['a', 'b']), [])
        self.assertEqual(multisplit('a+c', ['+']), ['a', 'c'])
        self.assertEqual(multisplit('a+aa+', ['+']), ['a', 'aa'])
        self.assertEqual(multisplit('a*aaa+b', ['+b', '*']), ['a', 'aaa'])
    def test_keep_empty_splits(self):
        self.assertEqual(multisplit('', ['a'], keep_empty=True), [''])
        self.assertEqual(multisplit('a', ['a', 'b'], keep_empty=True), ['', ''])
        self.assertEqual(multisplit('ab', ['a', 'b'], keep_empty=True), ['', '', ''])
        self.assertEqual(multisplit('a+aa', ['+'], keep_empty=True), ['a', 'aa'])
        self.assertEqual(multisplit('a+aab', ['+', 'b'], keep_empty=True), ['a', 'aa', ''])
        self.assertEqual(multisplit('a+**aa**', ['+', '**'], keep_empty=True), ['a', '', 'aa', ''])
    def test_keep_delims_splits(self):
        self.assertEqual(multisplit('', ['a'], keep_delims=True), [])
        self.assertEqual(multisplit('a', ['a', 'b'], keep_delims=True), ['a'])
        self.assertEqual(multisplit('aa', ['a', 'b'], keep_delims=True), ['a', 'a'])
        self.assertEqual(multisplit('ab', ['a'], keep_delims=True), ['a', 'b'])
        self.assertEqual(multisplit('a+aa', ['+'], keep_delims=True), ['a', '+', 'aa'])
        self.assertEqual(multisplit('a++aab', ['b', '+', '*'], keep_delims=True), ['a', '+', '+', 'aa', 'b'])
        self.assertEqual(multisplit('a+b*cd+*e', ['+', '*'], keep_delims=True), ['a', '+', 'b', '*', 'cd', '+', '*', 'e'])
    def test_keep_both_splits(self):
        self.assertEqual(multisplit('', ['a'], keep_delims=True, keep_empty=True), [''])
        self.assertEqual(multisplit('a', ['a', 'b'], keep_delims=True, keep_empty=True), ['', 'a', ''])
        self.assertEqual(multisplit('aa', ['a', 'b'], keep_delims=True, keep_empty=True), ['', 'a', '', 'a', ''])
        self.assertEqual(multisplit('abaa', ['b'], keep_delims=True, keep_empty=True), ['a', 'b', 'aa'])
        self.assertEqual(multisplit('a++aab', ['b', '+', '*'], keep_delims=True, keep_empty=True), ['a', '+', '', '+', 'aa', 'b', ''])
        self.assertEqual(multisplit('a+b*cd+*e', ['+', '*'], keep_delims=True, keep_empty=True), ['a', '+', 'b', '*', 'cd', '+', '', '*', 'e'])


def test():
    unittest.main()


if __name__ == '__main__':
    test()

