import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_selection_sort(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_insertion_sort(self):
        nums = [23, 10, 15, 13, 0]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [0, 10, 13, 15, 23])
        self.assertEqual(comps, 8)

if __name__ == '__main__': 
    unittest.main()
