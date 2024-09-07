import unittest
from main import flatmap


class TestFlatMap(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(flatmap([], lambda _: range(5)), [])
    def test_empty_output(self):
        self.assertEqual(flatmap(range(5), lambda _: []), [])
    def test_unary_return(self):
        self.assertEqual(flatmap(range(5), lambda val: [val]), list(range(5)))
        self.assertEqual(flatmap(range(5), lambda val: [2 * val]), [2 * val for val in range(5)])
    def test_multi_return(self):
        self.assertEqual(flatmap([0, 1], lambda val: [val, val]), [0, 0, 1, 1])
        self.assertEqual(flatmap([0, 3, 2], lambda val: [val] * val), [3, 3, 3, 2, 2])
    def test_enumerable_return(self):
        self.assertEqual(flatmap(enumerate([9, 7, 5]), lambda item: [item[1]]*item[0]), [7, 5, 5])


def test():
    unittest.main()


if __name__ == '__main__':
    test()

