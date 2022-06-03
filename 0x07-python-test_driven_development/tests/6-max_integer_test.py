#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def valid_test(self):
        """
    Unittest for max_integer([..])
        """
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([5.6, 3, 4, 2]), 5.6)
        self.assertEqual(max_integer(["bueno", "hola", "a", "hi"]), "hola")
        self.assertEqual(max_integer([-1, -2, -30, -6]), -1)
        self.assertEqual(max_integer([[1, 2], [1, 2, 3], [1]]), [1, 2, 3])
        self.assertEqual(max_integer([]), None)

    def faild_test(self):
        """
    Unittest for max_integer([..])
        """
        self.assertRaises(TypeError, max_integer, (["hola", [1, 2, 3], [1]]))
        self.assertRaises(TypeError, max_integer, (["h", 2, 1]))
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, (["a", 3.2, 5]))
        self.assertRaises(TypeError, max_integer, (["a", [1, 2], 5]))
