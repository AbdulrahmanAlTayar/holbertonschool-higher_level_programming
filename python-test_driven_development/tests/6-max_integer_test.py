#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_work_on_a_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_work_on_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_on_an_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_a_list_of_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_begining(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_with_negative_numbers(self):
        self.assertEqual(max_integer([-4, 2, 3, 1]), 3)

    def test_with_only_negatives(self):
        self.assertEqual(max_integer([-2, -5, -1, -99]), -1)


if __name__ == "__main__":
    unittest.main()
