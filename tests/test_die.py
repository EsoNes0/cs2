# -*- coding: utf-8 -*-
"""tests for virtual die"""

import unittest
from structures.die import Die


class test_Die(unittest.TestCase):
    """test class for virtual die"""

    def test_zero(self):
        """die test method"""
        die = Die(0)
        self.assertEqual(die.roll(), 0)

    def test_negative(self):
        """die test method"""
        die = Die(0)
        self.assertEqual(die.roll(), 0)

    def test_bounds(self):
        """die test method"""
        die = Die(10)
        self.assertLessEqual(die.roll(), 10)
        self.assertGreaterEqual(die.roll(), 1)
