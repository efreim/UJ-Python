import unittest
from rectangles import Rectangle

class TestRectangles(unittest.TestCase):

    def setUp(self):
        self.one = Rectangle(1, 2, 3, 4)
        self.two = Rectangle(2, 2, 2, 2)
        self.three = Rectangle(0, 1, 0, -1)

    def test_center(self):
        self.assertEqual(self.one.center(), '(2.0, 3.0)')
        self.assertEqual(self.two.center(), '(2.0, 2.0)')
        self.assertEqual(self.three.center(), '(0.0, 0.0)')

    def test_area(self):
        self.assertEquals(self.one.area(), 4)
        self.assertEquals(self.two.area(), 0)
        self.assertEquals(self.three.area(), 0)

    def test_move(self):
        self.assertEquals(self.one.move(1, 1), '[(2, 3),(4, 5)]')
        self.assertEquals(self.two.move(0, 0), '[(2, 2),(2, 2)]')
        self.assertEquals(self.three.move(-1, -1), '[(-1, 0),(-1, -2)]')

if __name__ == '__main__':
    unittest.main()