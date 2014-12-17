import unittest
from rectangles import Rectangle

class TestRectangles(unittest.TestCase):

    def setUp(self):
        self.one = Rectangle(1, 2, 3, 4)
        self.two = Rectangle(2, 2, 2, 2)
        self.three = Rectangle(0, 0, 2, 2)

    def test_center(self):
        self.assertEqual(self.one.center(), '(2.0, 3.0)')
        self.assertEqual(self.two.center(), '(2.0, 2.0)')
        self.assertEqual(self.three.center(), '(1.0, 1.0)')

    def test_area(self):
        self.assertEquals(self.one.area(), 4)
        self.assertEquals(self.two.area(), 0)
        self.assertEquals(self.three.area(), 4)

    def test_move(self):
        self.assertEquals(self.one.move(1, 1), '[(2, 3),(4, 5)]')
        self.assertEquals(self.two.move(0, 0), '[(2, 2),(2, 2)]')
        self.assertEquals(self.three.move(-1, -1), '[(-1, -1),(1, 1)]')

    def test_intersection(self):
        self.assertEqual(self.three.intersection(Rectangle(-1, -1, 1, 1)), Rectangle(0, 0, 1, 1))
        self.assertEqual(self.three.intersection(Rectangle(1, 1, 3, 3)), Rectangle(1, 1, 2, 2))
        self.assertEqual(self.three.intersection(Rectangle(0, 1, 2, 3)), Rectangle(0, 1, 2, 2))

    def test_cover(self):
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(0, 2, 1, 3)), Rectangle(0, 0, 1, 3))
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(2, 0, 3, 1)), Rectangle(0, 0, 3, 1))
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(0, -2, 1, -1)), Rectangle(0, -2, 1, 1))
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(-2, 0, -1, 1)), Rectangle(-2, 0, 1, 1))
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(2, 2, 3, 3)), Rectangle(0, 0, 3, 3))
        self.assertEquals(Rectangle(0, 0, 1, 1).cover(Rectangle(-3, -3, -2, -2)), Rectangle(-3, -3, 1, 1))

    def text_make4(self):
        self.assertEquals(self.rec_two.make4(), [Rectangle(2, 2, 1, 1),
                                                Rectangle(1, 1, 2, 2),
                                                 Rectangle(2, 1, 1, 2),
                                                 Rectangle(1, 2, 2, 1)])

if __name__ == '__main__':
    unittest.main()