import unittest

import fracs


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 3], [1, 4]), [7, 12])
        self.assertEqual(fracs.add_frac([2, 2], [1, 2]), [3, 2])
        self.assertEqual(fracs.add_frac([5, 2], [1, 2]), [6, 2])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([2, 3], [1, 3]), [1, 3])
        self.assertEqual(fracs.sub_frac([1, 3], [1, 3]), [0, 3])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1, 4], [1, 4]), [1, 16])
        self.assertEqual(fracs.mul_frac([2, 3], [2, 3]), [4, 9])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1, 2], [1, 2]), [2, 2])
        self.assertEqual(fracs.div_frac([2, 3], [1, 2]), [4, 3])

    def test_is_positive(self):
        self.assertEqual(fracs.is_positive([1, 2]), True)
        self.assertEqual(fracs.is_positive([4, 6]), True)
        self.assertEqual(fracs.is_positive([-2, -4]), True)
        self.assertEqual(fracs.is_positive([-2, 3]), False)


    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([2, 10]), 0.2)

    def test_is_zero(self):
        self.assertEqual(fracs.is_zero([0, 4]), True)
        self.assertEqual(fracs.is_zero([2, 3]), False)


if __name__ == '__main__':
    unittest.main()