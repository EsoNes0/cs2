# -*- coding: utf-8 -*-
"""Basic tests for recurive string replacement """

import unittest
from cs2.recursive_string_replace import findandreplace
# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement
# pylint: disable=missing-class-docstring


class TestFindAndReplace(unittest.TestCase):
    def test_all_none(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace(None, None, None), None)

    def test_find_none(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

    def test_find_empty(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

    def test_replace_none(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

    def test_string_none(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace("a", "b", None), None)

    def test_simple(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

    def test_remove(self):
        """test method for recursive string replacement"""
        self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

    def test_gettysburg(self):
        """test method for recursive string replacement"""
        self.assertEqual(
            findandreplace(
                "Four score",
                "Twenty",
                "Four score and seven years ago"),
            "Twenty and seven years ago")
