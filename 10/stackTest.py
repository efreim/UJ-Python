import unittest
from stack import Stack


class TextStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(2)
        self.stack.push(5)
        self.stack.push(3)
        self.stack.push(1)
        self.stack.push(8)

        self.stackTwo = Stack()
        self.stackTwo.push(1)
        self.stackTwo.push(2)

    def test_push(self):
        self.stack.push(9)
        self.assertEquals(self.stack.__str__(), [2, 5, 3, 1, 8, 9])
        with self.assertRaises(IndexError):
            self.stack.push(4)
            self.stack.push(2)

    def test_pop(self):
        self.stackTwo.pop()
        self.assertEquals(self.stackTwo.__str__(), [1, None, None, None, None, None])
        with self.assertRaises(IndexError):
            self.stackTwo.pop()
            self.stackTwo.pop()
            self.stackTwo.pop()


if __name__ == '__main__':
    unittest.main()