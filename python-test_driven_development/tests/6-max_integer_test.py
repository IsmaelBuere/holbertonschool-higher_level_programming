#!/usr/bin/python3
"""Unittest fro max_integer([..])"""


import unittest
from your_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([-3]), -3)

        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2.5]), 3.5)

        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

        with self.assertRaises(TypeError):
            max_integer([1, 'a', 2, 'b'])

if __name__ == '__main__':
    unittest.main()

