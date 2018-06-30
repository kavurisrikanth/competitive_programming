import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.forward = []
        self.backward = []

        self.added_new = False
        self.removed_new = False

    def enqueue(self, item):
        if self.removed_new:
            self.forward = self.backward[::-1]
            self.removed_new = False

        self.forward.append(item)
        self.added_new = True

    def dequeue(self):
        if self.added_new:
            self.backward = self.forward[::-1]
            self.added_new = False

        self.removed_new = True
        return self.backward.pop()


# Tests

class Test(unittest.TestCase):

    def test_queue_usage(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)