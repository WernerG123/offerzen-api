import unittest
import bubbleSort
from bubbleSort import *

class TestStringMethods(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(Sorter.sort([5,4,2,3,1]), [1,2,3,4,5])

    def test_biglist(self):
        my_list = []
        for x in range(10000):
            my_list.append(int(x))
        self.assertRaises(ValueError, Sorter.sort, my_list)

    def test_nested(self):
        self.assertEqual(Sorter.sort([6,2,[4,3],[5,8,7], 1]), [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()