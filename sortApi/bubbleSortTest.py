import unittest
import bubbleSort
from bubbleSort import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(Sorter.sort([5,4,2,3,1]), [1,2,3,4,5])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()