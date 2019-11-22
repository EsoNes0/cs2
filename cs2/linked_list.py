from __future__ import print_function
import unittest
'''
    Description: Single linked list implementation
    Author: Larsen Close
    Version: Completed through extra credit level work with implementation and tests for extra methods
    Outline and initial tests provided in class by Professor Dr. Beaty at MSU Denver
'''

''' when run with "-m unittest", the following produces:
    FAILED (failures=9, errors=2)
    your task is to fix the failing tests by implementing the necessary
    methods. '''


class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        ''' no need for get or set, we only access the values inside the
            LinkedList class. and really: never have setters. '''

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        self.front = self.back = self.current = None
        if initial is not None:
            for x in initial:
                self.push_front(x)

    def empty(self):
        return self.front == self.back is None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def push_front(self, value):
        new = self.Node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    ''' you need to(at least) implement the following three methods'''

    def pop_front(self):
        if self.empty():
            raise RuntimeError("Empty List")
        tmp = self.front.value
        if self.front == self.back is not None:
            self.front = self.back = None
            return tmp
        else:
            self.front = self.front.next_node
            return tmp

    def push_back(self, value):
        new = self.Node(value, None)
        if self.empty():
            self.front = self.back = new
        else:
            self.back.next_node = new
            self.back = new

    def pop_back(self):
        if self.empty():
            raise RuntimeError("Empty List")
        tmp = self.back.value
        previous = None
        current = self.front
        if self.front == self.back is not None:
            self.front = self.back = None
            return tmp
        else:
            while current.next_node is not None:
                previous = current
                current = current.next_node
            self.back = previous
            self.back.next_node = None
            return tmp

    def __str__(self):
        tmp = ""
        while self.front.next_node is not None:
            tmp = tmp + str(self.pop_back()) + ", "
        tmp = tmp + str(self.pop_back())
        return tmp

    def __repr__(self):
        return 'LinkedList((' + str(self) + '))'

    def delete_value(self, value):
        previous = None
        current = self.front
        if (self.front == self.back is not None) and (
                self.front.value == value):
            self.front.next_node = None
            self.front = self.back = None
            return
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.front = self.front.next_node
                    return
                if current == self.back:
                    self.back = previous
                    return
                elif previous:
                    previous.next_node = current.next_node
                    return
            previous = current
            current = current.next_node
        else:
            raise RuntimeError("Value not present")

    def find_mid(self):
        if self.empty():
            raise RuntimeError("list empty")
        fast = self.front
        slow = self.front
        while (fast.next_node is not None) and (fast.next_node.next_node):
            fast = fast.next_node.next_node
            slow = slow.next_node
        return slow.value


if '__main__' == __name__:
    unittest.main()
