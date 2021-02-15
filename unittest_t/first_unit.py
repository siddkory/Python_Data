import unittest


class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum([3, 6, 9]), 18, "Sum should be 18")
        self.assertEqual(sum([3, 6, 9]) == 18, True, "Sum should be 18")

    def test_sub(self):
        self.assertEqual(6 - 3, 3, " Diff should be 3")
        self.assertEqual(6 - 3 == 3, True, " Diff should be 3")


if __name__ == "__main__":
    unittest.main()
