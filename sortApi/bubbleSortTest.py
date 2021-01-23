import unittest
import bubbleSort
from bubbleSort import *

class TestStringMethods(unittest.TestCase):
# Basic bubble sort test
    def test_basic(self):
        self.assertEqual(Sorter.sort([5,4,2,3,1]), [1,2,3,4,5])

# Test to check exception for lists with more than 9999 items
    def test_biglist(self):
        my_list = []
        for x in range(10000):
            my_list.append(int(x))
        self.assertRaises(ValueError, Sorter.sort, my_list)

# Test nested list - Interesting how the results differ if I dont convert to str on line 18...WTF?
    def test_nested(self):
        self.assertEqual(Sorter.sort(str([6,2,[4,3],[[5,8],7], 1])), [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()