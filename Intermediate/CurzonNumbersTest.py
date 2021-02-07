import unittest
"""A number N is said to be a Curzon Number if 2**N + 1 is divisible by 2*N + 1.
"""


def is_curzon(num):
    exp = 2 ** num + 1
    mul = 2 * num + 1
    r = exp / mul
    print(int(r))
    print(r)
    return exp % mul == 0


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_curzon(5), True)
        self.assertEqual(is_curzon(10), False)
        self.assertEqual(is_curzon(14), True)
        self.assertEqual(is_curzon(86), True)
        self.assertEqual(is_curzon(90), True)
        self.assertEqual(is_curzon(115), False)
        self.assertEqual(is_curzon(120), False)
        self.assertEqual(is_curzon(194), True)
        self.assertEqual(is_curzon(293), True)


if __name__ == '__main__':
    unittest.main()