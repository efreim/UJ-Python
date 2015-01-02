import unittest
from queue import Queue


class TextStack(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.put(4)
        self.queue.put(2)
        self.queue.put(1)
        self.queue.put(6)

        self.queueTwo = Queue()
        self.queueTwo.put(1)
        self.queueTwo.put(2)


    def test_put(self):
        self.queue.put(9)
        self.assertEquals(self.queue.__str__(), [4, 2, 1, 6, 9, None])
        with self.assertRaises(IndexError):
            self.queue.put(1)
            self.queue.put(2)

    def test_pop(self):
        self.queueTwo.get()
        self.assertEquals(self.queueTwo.__str__(), [None, 2, None, None, None , None])
        with self.assertRaises(IndexError):
            self.queueTwo.get()
            self.queueTwo.get()


if __name__ == '__main__':
    unittest.main()