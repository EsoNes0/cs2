# -*- coding: utf-8 -*-
"""Basic tests for the binary search tree"""


import unittest
from structures.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    """Basic test class for binary tree"""

    def test_empty(self):
        """Basic test method for binary tree"""
        self.assertTrue(BinaryTree().empty())

    def test_insert(self):
        """Basic test method for binary tree"""
        bt = BinaryTree()
        bt.insert(20)
        bt.insert(10)
        bt.insert(30)
        bt.insert(25)
        bt.insert(35)
        self.assertEqual(str(bt), '10,20,25,30,35')

    def test_remove_left_leaf(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(25)
        self.assertEqual(str(bt), '10,20,30,35')

    def test_remove_leaf_right(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(35)
        self.assertEqual(str(bt), '10,20,25,30')

    def test_remove_only_left(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 5, 30, 25, 35])
        bt.remove(10)
        self.assertEqual(str(bt), '5,20,25,30,35')

    def test_remove_only_right(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 15, 30, 25, 35])
        bt.remove(10)

    def test_remove_both(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 15, 30, 25, 35])
        bt.remove(30)
        self.assertEqual(str(bt), '10,15,20,25,35')

    '''
      20
     /  \
    10  30
       /  \
      25  35
     /
    24
    '''

    def test_remove_both_again(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 24, 35])
        bt.remove(30)
        self.assertEqual(str(bt), '10,20,24,25,35')

    '''
      20
     /  \
    10  30
       /  \
      25  35
     / \
    24 27
    '''

    def test_double_recursion(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 24, 27, 35])
        bt.remove(30)
        self.assertEqual(str(bt), '10,20,24,25,27,35')

    def test_remove_root(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 35])
        bt.remove(20)
        self.assertEqual(str(bt), '10,25,30,35')

    def test_init(self):
        """Basic test method for binary tree"""
        bt = BinaryTree([20, 10, 30, 25, 35])
        self.assertEqual(str(bt), '10,20,25,30,35')
