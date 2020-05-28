# -*- coding: utf-8 -*-
'''Singly linked list implementation


Author: Larsen Close
Version: Completed through extra credit level work with implementation and
tests for extra methods
Outline and initial tests provided in class by Professor Dr. Beaty at
MSU Denver


Todo:
    * Make runnable from file
    * Also also use ``sphinx.ext.todo`` extension
'''


class LinkedList():
    '''Singly linked list class'''
    class Node():
        '''Node class for the linked list'''

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        self.front = self.back = self.current = None
        if initial is not None:
            for x in initial:
                self.push_front(x)

    def empty(self):
        '''empty method for linked list returns empty list'''
        return self.front == self.back is None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        raise StopIteration()

    def push_front(self, value):
        '''push front method for linked list, takes value pushes onto front'''
        new = self.Node(value, self.front)
        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    def pop_front(self):
        '''pop front method for linked list, removes value from list front'''
        if self.empty():
            raise RuntimeError("Empty List")
        tmp = self.front.value
        if self.front == self.back is not None:
            self.front = self.back = None
            return tmp
        self.front = self.front.next_node
        return tmp

    def push_back(self, value):
        '''push back method for linked list, takes value pushes onto back'''
        new = self.Node(value, None)
        if self.empty():
            self.front = self.back = new
        else:
            self.back.next_node = new
            self.back = new

    def pop_back(self):
        '''pop back method for linked list, removes value from list back'''
        if self.empty():
            raise RuntimeError("Empty List")
        tmp = self.back.value
        previous = None
        current = self.front
        if self.front == self.back is not None:
            self.front = self.back = None
            return tmp
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
        '''delete method for linked list, removes value from list'''
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
                previous.next_node = current.next_node
                return
            previous = current
            current = current.next_node
        raise RuntimeError("Value not present")

    def find_mid(self):
        '''find mid method for linked list, returns list middle'''
        if self.empty():
            raise RuntimeError("list empty")
        fast = self.front
        slow = self.front
        while (fast.next_node is not None) and (fast.next_node.next_node):
            fast = fast.next_node.next_node
            slow = slow.next_node
        return slow.value
