# -*- coding: utf-8 -*-
'''Dijkstra's algorithm implementation


A recursive method that takes 1) a string to find, 2) a string to replace
the found string with, and 3) an initial string. Return the initial string with
all the found strings replaced with the replacement string. Without using loops
or the built-in string methods except comparison, length, and slicing.


Author: Larsen Close
Version: Completed through A level work
Outline and initial tests provided in class by Professor Dr. Beaty at
MSU Denver


Todo:
    * Make runnable from file
    * Also also use ``sphinx.ext.todo`` extension
'''

import sys


TRACK_PREVIOUS = True


class WeightedDigraph:
    '''Weighted digraph class for dijkstra's algorithm implementation'''
    class _edge():
        def __init__(self, to_node, weight):
            self.to_node = to_node
            self.weight = weight

    class _node():
        def __init__(self, value):
            self.value = value
            self.edges = []

        def __str__(self):
            resultant = str(self.value)
            for edge in self.edges:
                resultant += "->" + str(edge.to_node.value) + \
                          "(" + str(edge.weight) + ")"
            return resultant

        def add_edge(self, new_edge):
            '''add edge method for weighted digraph class'''
            if not self.is_adjacent(new_edge.to_node):
                self.edges.append(new_edge)

        def remove_edge(self, to_node):
            '''remove edge method for weighted digraph class'''
            for edge in self.edges:
                if edge.to_node == to_node:
                    self.edges.remove(edge)

        def is_adjacent(self, node):
            '''checks adjanency to single node'''
            for edge in self.edges:
                if edge.to_node == node:
                    return True
            return False

    def __init__(self, directed=True):
        self.__nodes = []
        self.__directed = directed

    def __len__(self):
        return len(self.__nodes)

    def __str__(self):
        resultant = ""
        for node in self.__nodes:
            resultant += str(node) + '\n'
        return resultant

    def __iter__(self):
        return iter(self.__nodes)

    def find(self, value):
        '''find method for weighted digraph class'''
        for node in self:
            if node.value == value:
                return node

        return None

    def add_nodes(self, nodes):
        '''add nodes plural method, calls add node'''
        for node in nodes:
            self.add_node(node)

    def add_node(self, value):
        '''add node method for weighted digraph class'''
        if not self.find(value):
            self.__nodes.append(self._node(value))

    def add_edges(self, edges):
        '''add edges plural method, calls add edge'''
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    def add_edge(self, from_value, to_value, weight):
        '''add edge method for weighted digraph class'''
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        if not from_node:
            self.add_node(from_value)
            from_node = self.find(from_value)
        if not to_node:
            self.add_node(to_value)
            to_node = self.find(to_value)

        from_node.add_edge(self._edge(to_node, weight))
        if not self.__directed:
            to_node.add_edge(self._edge(from_node, weight))

    def remove_edge(self, from_value, to_value):
        '''remove edge method for weighted digraph class'''
        from_node = self.find(from_value)
        to_node = self.find(to_value)

        from_node.remove_edge(to_node)
        if not self.__directed:
            to_node.remove_edge(from_node)

    def are_adjacent(self, value1, value2):
        '''method to check if two nodes are adjacent'''
        return self.find(value1).is_adjacent(self.find(value2))

    def infandnone(self):
        '''changes distance to unbound upper limit and previous to none '''
        for node in self:
            node.distance = float("inf")
            node.previous = None

    def track_previous(self, end):
        '''method for tracking the previous paths'''
        _path = []
        last = self.find(end)
        while last.previous is not None:
            _path.append(last.previous.value)
            last = last.previous

        return _path

    def dijkstra(self, start):
        '''dijkstras implementation'''

        if not self:
            raise RuntimeError("no graph")

        if len(self) == 1:
            for node in self:
                node.distance = 0
                node.previous = None
                return False

        self.infandnone()
        source = self.find(start)
        source.distance = 0
        if not source:
            raise RuntimeError("source not found")

        todo = set()
        todo.add(source)

        result = []

        while todo:

            smallest = float("inf")

            for node in todo:

                if node.distance < smallest:
                    _min = node
                    smallest = node.distance

            todo.remove(_min)
            result.append([_min.distance, _min.value])

            for edge in _min.edges:
                alt = _min.distance + edge.weight

                if alt < edge.to_node.distance:
                    edge.to_node.distance = alt
                    edge.to_node.previous = _min

                    todo.add(edge.to_node)

        for item in result:
            item.extend(self.track_previous(item[1]))

        return result


if __name__ == '__main__':
    GRAPH = WeightedDigraph(False)
    FILE = open(sys.argv[1], "r")
    for line in FILE:
        a = line.strip().split(" ")
        GRAPH.add_edge(a[0], a[1], int(a[2]))
    RESULTING = GRAPH.dijkstra("Denver")
    for city in RESULTING:
        print(city[1], "is", city[0], 'miles from Denver')
        if TRACK_PREVIOUS:
            for path in city[2:]:
                print("     ", path)
