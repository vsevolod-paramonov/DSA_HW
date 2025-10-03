import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_add_del(self):
        queue = Queue()
        queue.add_to_queue(1)
        queue.add_to_queue(2)
        queue.add_to_queue(3)
        self.assertEqual(queue.delete_from_queue(), 1)
        self.assertEqual(queue.delete_from_queue(), 2)
        self.assertEqual(queue.delete_from_queue(), 3)

    def test_empty_delete_from_queue(self):
        queue = Queue()
        self.assertIsNone(queue.delete_from_queue())

    def test_mixed_operations(self):
        queue = Queue()
        queue.add_to_queue(5)
        queue.add_to_queue(10) 
        self.assertEqual(queue.delete_from_queue(), 5)
        queue.add_to_queue(15)
        self.assertEqual(queue.delete_from_queue(), 10)
        self.assertEqual(queue.delete_from_queue(), 15)

if __name__ == "__main__":
    unittest.main()