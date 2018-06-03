import bullets as bul
import unittest

class TestList(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(bul.distance(-2, 0, 2, -1, 4), 0)

    def test_projection(self):
        self.assertEqual(bul.projection(-2, 0, [-2, 1, -4]), [-2, 0])

    def test_one_crossing(self):
        self.assertEqual(bul.one_crossing([0, 0], [1, 0], 2, 2, 1), False)
        self.assertEqual(bul.one_crossing([0, 0], [1, 0], 2, 0, 1.4), True)

    def test_crossing(self):
        self.assertEqual(bul.crossing([[0, 0], [0, 3], [3, 3], [3, 0]], 2, 2, 1), True)
        self.assertEqual(bul.crossing([[0, 0], [0, 3], [3, 3], [3, 0]], 2, 2, 0.5), False)


