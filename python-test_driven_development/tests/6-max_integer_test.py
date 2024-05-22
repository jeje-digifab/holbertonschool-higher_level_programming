#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer())

    def test_one_int_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list(self):
        self.assertEqual(max_integer([1, 10, 15]), 15)

    def test_one_int_neg_list(self):
        self.assertEqual(max_integer([10, 1, -5]), 10)

    def test_int_neg_list(self):
        self.assertEqual(max_integer([-1, -5, -7]), -1)

    def test_rep_int_list(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
