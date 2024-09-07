import unittest
from main import split 


class TestSplit(unittest.TestCase):
    def test_empty_delims(self):
        with self.assertRaises(ValueError):
            split('abc', '')
    def test_splits(self):
        self.assertEqual(split('', 'a'), [])
        self.assertEqual(split('a', 'a'), [])
        self.assertEqual(split('aa', 'a'), [])
        self.assertEqual(split('abc', 'b'), ['a', 'c'])
        self.assertEqual(split('abbaabb', 'bb'), ['a', 'aa'])
        self.assertEqual(split('abbaaab', 'b'), ['a', 'aaa'])
    def test_keep_empty_splits(self):
        self.assertEqual(split('', 'a', keep_empty=True), [''])
        self.assertEqual(split('a', 'a', keep_empty=True), ['', ''])
        self.assertEqual(split('aa', 'a', keep_empty=True), ['', '', ''])
        self.assertEqual(split('abaa', 'b', keep_empty=True), ['a', 'aa'])
        self.assertEqual(split('abbaabb', 'bb', keep_empty=True), ['a', 'aa', ''])
        self.assertEqual(split('abbaab', 'b', keep_empty=True), ['a', '', 'aa', ''])
    def test_keep_delims_splits(self):
        self.assertEqual(split('', 'a', keep_delims=True), [])
        self.assertEqual(split('a', 'a', keep_delims=True), ['a'])
        self.assertEqual(split('aa', 'a', keep_delims=True), ['a', 'a'])
        self.assertEqual(split('ab', 'a', keep_delims=True), ['a', 'b'])
        self.assertEqual(split('abaa', 'b', keep_delims=True), ['a', 'b', 'aa'])
        self.assertEqual(split('abbaabb', 'bb', keep_delims=True), ['a', 'bb', 'aa', 'bb'])
        self.assertEqual(split('abbaab', 'b', keep_delims=True), ['a', 'b', 'b', 'aa', 'b'])
    def test_keep_both_splits(self):
        self.assertEqual(split('', 'a', keep_delims=True, keep_empty=True), [''])
        self.assertEqual(split('a', 'a', keep_delims=True, keep_empty=True), ['', 'a', ''])
        self.assertEqual(split('aa', 'a', keep_delims=True, keep_empty=True), ['', 'a', '', 'a', ''])
        self.assertEqual(split('abaa', 'b', keep_delims=True, keep_empty=True), ['a', 'b', 'aa'])
        self.assertEqual(split('abbaabb', 'bb', keep_delims=True, keep_empty=True), ['a', 'bb', 'aa', 'bb', ''])
        self.assertEqual(split('abbaab', 'b', keep_delims=True, keep_empty=True), ['a', 'b', '', 'b', 'aa', 'b', ''])


def test():
    unittest.main()


if __name__ == '__main__':
    test()

