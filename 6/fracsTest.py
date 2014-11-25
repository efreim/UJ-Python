import unittest
from fracs import Frac

class TestFracs(unittest.TestCase):

    def setUp(self):
        self.one = Frac(1, 2)
        self.two = Frac(1, 4)
        self.three = Frac(-1, 6)
        self.four = Frac(0, 6)
        self.five = Frac(-2, 5)

    def test_cmp(self):
        self.assertEqual(self.three.__cmp__(self.four), -1)
        self.assertEqual(self.three.__cmp__(self.three), 0)
        self.assertEqual(self.three.__cmp__(self.five), 1)

    def test_add(self):
        self.assertEqual(self.one.__add__(self.two), Frac(3, 4))
        self.assertEqual(self.one.__add__(self.four), Frac(3, 6))
        self.assertEqual(self.one.__add__(self.five), Frac(1, 10))


    def test_sub(self):
        self.assertEqual(self.one.__sub__(self.two), Frac(1, 4))

    def test_mul(self):
        self.assertEqual(self.two.__mul__(self.two), Frac(1, 16))

    def test_div(self):
        self.assertEqual(self.three.__div__(self.two), Frac(-2, 3))

    def test_pos(self):
        self.assertEqual(self.one.__pos__(), Frac(1, 2))

    def test_neg(self):
        self.assertEqual(self.one.__neg__(), Frac(-1, 2))

    def test_invert(self):
        self.assertEqual(self.two.__invert__(), Frac(4, 1))

    def test_is_positive(self):
        self.assertEqual(self.one.is_positive(), True)
        self.assertEqual(self.five.is_positive(), False)

    def test_is_zero(self):
        self.assertEqual(self.two.is_zero(), False)
        self.assertEqual(self.four.is_zero(), True)

    def test_frac_to_float(self):
        self.assertEqual(self.five.frac2float(), -0.4)
        self.assertEqual(self.two.frac2float(), 0.25)

if __name__ == '__main__':
    unittest.main()