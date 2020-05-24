# -*- coding: utf-8 -*-
"""Basic tests for all queens problem"""

import unittest
from structures.all_queens import AllQueens
# pylint: disable=invalid-name


class Test_Safe(unittest.TestCase):
    """Basic tests for all queens problem"""

    def test_same(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertFalse(queen.safe(1, 1, 1, 1))

    def test_same_row(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertFalse(queen.safe(1, 1, 1, 2))

    def test_same_column(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertFalse(queen.safe(1, 1, 2, 1))

    def test_same_diagonal(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertFalse(queen.safe(1, 1, 5, 5))


class test_one(unittest.TestCase):
    """Basic tests for all queens problem"""

    def test_one_one(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertTrue(queen.solve_one(1, 0, []))

    def test_two_all(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertEqual(queen.solve_one(2, 0, []), [(0, 0)])

    def test_four_one(self):
        """Basic tests for all queens problem"""
        queen = AllQueens()
        self.assertEqual(queen.solve_one(4, 0, []), [
            (0, 0), (1, 2), (2, 0), (3, 1)])


class test_all(unittest.TestCase):
    queen = AllQueens()
    def test_one_all(self):
        self.assertEqual(queen.solve_all(1, 0, [], []), [[(0, 0)]])
    def test_two_all(self):
        self.assertEqual(queen.solve_all(2, 0, [], []), [])
    def test_three_all(self):
        self.assertEqual(queen.solve_all(3, 0, [], []), [])
    def test_four_all(self):
        solutions = queen.solve_all(4, 0, [], [])
        self.assertEqual(solutions, [[(0, 1), (1, 3), (2, 0), (3, 2)], \
            [(0, 2), (1, 0), (2, 3), (3, 1)]])

