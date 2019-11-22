# -*- coding: utf-8 -*-
"""Basic tests for linked list"""

import unittest
from cs2.linked_list import LinkedList
# pylint: disable=invalid-name
# pylint: disable=pointless-string-statement
# pylint: disable=missing-class-docstring


class TestEmpty(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        self.assertTrue(LinkedList().empty())


class TestPushFrontPopBack(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        self.assertTrue(linked_list.empty())


class TestPushFrontPopFront(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())


class TestPushBackPopFront(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())


class TestPushBackPopBack(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())


class TestInitialization(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList(("one", 2, 3.141592))
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3.141592)


class TestStr(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')


class TestRepr(unittest.TestCase):
    """Linked list testing class"""

    def test(self):
        """Testing linked list"""
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')


class TestErrors(unittest.TestCase):
    """Linked list testing class"""

    def test_pop_front_empty(self):
        """Testing linked list"""
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        """Testing linked list"""
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())


class TestDelete(unittest.TestCase):
    """Linked list testing class"""

    def test_delete_value(self):
        """Testing linked list"""
        linked_list = LinkedList((5, 3, 2, 8, 9))
        linked_list.delete_value(3)
        linked_list.delete_value(9)
        linked_list.delete_value(5)
        linked_list.delete_value(2)
        linked_list.delete_value(8)
        self.assertTrue(linked_list.empty())

    def test_delete_value_multi_instance(self):
        """Testing linked list"""
        linked_list = LinkedList((6, 6, 6))
        linked_list.delete_value(6)
        linked_list.delete_value(6)
        linked_list.delete_value(6)
        self.assertTrue(linked_list.empty())

    def test_delete_value_multi_instance_single_delete(self):
        """Testing linked list"""
        linked_list = LinkedList((6, 6, 6))
        linked_list.delete_value(6)
        self.assertFalse(linked_list.empty())

    def test_delete_value_multi(self):
        """Testing linked list"""
        linked_list = LinkedList((6, 6, 8, 6))
        linked_list.delete_value(6)
        linked_list.delete_value(6)
        linked_list.delete_value(6)
        self.assertFalse(linked_list.empty())

    def test_delete_value_missing(self):
        """Testing linked list"""
        self.assertRaises(RuntimeError, lambda: LinkedList().delete_value(9))


class TestFindMiddle(unittest.TestCase):
    """Linked list testing class"""

    def test_find_middle(self):
        """Testing linked list"""
        linked_list = LinkedList((5, 3, 2, 8, 9))
        self.assertEqual(linked_list.find_mid(), 2)

    def test_find_middle_longer(self):
        """Testing linked list"""
        linked_list = LinkedList(
            (5,
             3,
             2,
             8,
             9,
             11,
             23,
             28,
             67,
             99,
             82,
             190,
             12389,
             "foo",
             4.2938,
             123.1,
             90,
             1000,
             True))
        self.assertEqual(linked_list.find_mid(), 99)

    def test_find_middle_even(self):
        """Testing linked list"""
        linked_list = LinkedList((5, 3, 2, 8, 9, 11, 1, 9, 100, 14))
        # in even case, decided that second of two is middle
        self.assertEqual(linked_list.find_mid(), (11))

    def test_find_middle_even_long(self):
        """Testing linked list"""
        linked_list = LinkedList(
            (5,
             3,
             2,
             8,
             9,
             11,
             23,
             28,
             67,
             99,
             82,
             190,
             12389,
             "foo",
             4.2938,
             123.1,
             90,
             1000))
        # in even case, decided that second of two is middle
        self.assertEqual(linked_list.find_mid(), (99))

    def test_find_middle_single_node(self):
        """Testing linked list"""
        linked_list = LinkedList()
        linked_list.push_front(1)
        self.assertEqual(linked_list.find_mid(), 1)

    def test_find_middle_emptylist(self):
        """Testing linked list"""
        self.assertRaises(RuntimeError, lambda: LinkedList().find_mid())


# ''' extra credit.
#     - write test cases for and implement a delete(value) method.
#     - write test cases for and implement a method that finds the middle
#       element with only a single traversal.
# '''

# ''' the following is a demonstration that uses our data structure as a
#     stack'''


def fact(number):
    '''"Pretend" to do recursion via a stack and iteration'''

    if number < 0:
        raise ValueError("Less than zero")
    if number in (0, 1):
        return 1

    stack = LinkedList()
    while number > 1:
        stack.push_front(number)
        number -= 1

    result = 1
    while not stack.empty():
        result *= stack.pop_front()

    return result


class TestFactorial(unittest.TestCase):
    """Linked list testing class"""

    def test_less_than_zero(self):
        """Testing linked list"""
        self.assertRaises(ValueError, lambda: fact(-1))

    def test_zero(self):
        """Testing linked list"""
        self.assertEqual(fact(0), 1)

    def test_one(self):
        """Testing linked list"""
        self.assertEqual(fact(1), 1)

    def test_two(self):
        """Testing linked list"""
        self.assertEqual(fact(2), 2)

    def test_10(self):
        """Testing linked list"""
        self.assertEqual(fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
