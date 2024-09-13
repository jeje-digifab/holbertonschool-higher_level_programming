#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 5, 4, 2]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([10]), 10)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-3, -5, -1, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1, 100, -100]), 100)

    def test_all_same_numbers(self):
        """Test with a list where all numbers are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
