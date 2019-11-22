# -*- coding: utf-8 -*-
"""Tests for dijkstra algorithm"""


import unittest
from cs2.dijkstra import Weighted_Digraph, TRACK_PREVIOUS
# pylint: disable=invalid-name
# pylint: disable=no-value-for-parameter


class test_weighted_digraph(unittest.TestCase):
    """Weigted digraph class for dijkstras"""

    def test_empty(self):
        """Tests if digraph is empty"""
        self.assertEqual(len(Weighted_Digraph()), 0)

    def test_one(self):
        """Tests if digraph has one"""
        g = Weighted_Digraph()
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_duplicate(self):
        """Tests if digraph has duplicates"""
        g = Weighted_Digraph()
        g.add_node(1)
        g.add_node(1)
        self.assertEqual(len(g), 1)

    def test_two(self):
        """Tests if digraph has 2"""
        g = Weighted_Digraph()
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(len(g), 2)

    def test_edge(self):
        """Tests digraph edges"""
        g = Weighted_Digraph()
        g.add_node(1)
        g.add_node(2)
        g.add_edge(1, 2, 3)
        self.assertEqual(str(g), '1->2(3)\n2\n')

    def test_adding_ints(self):
        """Tests adding ints"""
        g = Weighted_Digraph()
        g.add_nodes([1, 2])
        g.add_edges([(1, 2, 3), (2, 1, 3)])
        self.assertEqual(str(g), '1->2(3)\n2->1(3)\n')

    def test_adding_strings(self):
        """Tests adding strings"""
        g = Weighted_Digraph()
        g.add_nodes(['Denver', 'Boston'])
        g.add_edges([('Denver', 'Boston', 1971.8),
                     ('Boston', 'Denver', 1971.8)])
        self.assertEqual(
            str(g), 'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def test_are_adjacent(self):
        """Tests adjacency"""
        g = Weighted_Digraph()
        g.add_nodes(['Denver', 'Boston'])
        g.add_edges([('Denver', 'Boston', 1971.8),
                     ('Boston', 'Denver', 1971.8)])
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent(self):
        """Tests non-adjacency"""
        g = Weighted_Digraph()
        g.add_nodes(['Denver', 'Boston', 'Milano'])
        g.add_edges([('Denver', 'Boston', 1971.8),
                     ('Boston', 'Denver', 1971.8)])
        self.assertFalse(g.are_adjacent('Denver', 'Milano'))

    def test_arent_adjacent_directed(self):
        """Tests non-adjacency directed"""
        g = Weighted_Digraph()
        g.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertFalse(g.are_adjacent('Denver', 'Milano'))
        self.assertFalse(g.are_adjacent('Boston', 'Denver'))
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_arent_adjacent_undirected(self):
        """Tests non-adjacency non-directed"""
        g = Weighted_Digraph(False)
        g.add_edges([('Denver', 'Boston', 1971.8)])
        self.assertTrue(g.are_adjacent('Boston', 'Denver'))
        self.assertTrue(g.are_adjacent('Denver', 'Boston'))

    def test_add_edges_without_nodes(self):
        """Tests adges without nodes"""
        g = Weighted_Digraph()
        g.add_edges([('Denver', 'Boston', 1971.8),
                     ('Boston', 'Denver', 1971.8)])
        self.assertEqual(str(g),
                         'Denver->Boston(1971.8)\nBoston->Denver(1971.8)\n')

    def empty_graph(self):
        """Testing dijkstras"""
        self.assertRaises(RuntimeError, lambda: Weighted_Digraph.dijkstra(0))

    def unfound_start(self):
        """Testing dijkstras"""
        g = Weighted_Digraph(False)
        g.add_nodes(["Denver"])
        self.assertRaises(
            RuntimeError, lambda: Weighted_Digraph.dijkstra(None))

    def test_infandnone(self):
        """Testing dijkstras"""
        g = Weighted_Digraph(False)
        g.add_edges([(1, 2, 2), (1, 3, 1), (2, 3, 1), (2, 4, 1),
                     (2, 5, 2), (3, 5, 5), (4, 5, 3), (4, 6, 6), (5, 6, 1)])
        g.infandnone()
        for node in g:
            self.assertEqual(node.distance, float("inf"))
            self.assertEqual(node.previous, None)

    # def test_two_element(self):
    #     """Testing dijkstras"""
    #     pass

    def test_dijkstra(self):
        """Testing dijkstras"""
        # '''
        #     2---1---4
        #    /|\      |\
        #   2 | \     | 6
        #  /  |  \    |  \
        # 1   1   2   3   6
        #  \  |    \  |  /
        #   1 |     \ | 1
        #    \|      \|/
        #     3---5---5
        # '''
        g = Weighted_Digraph(False)
        g.add_edges([(1, 2, 2), (1, 3, 1), (2, 3, 1), (2, 4, 1),
                     (2, 5, 2), (3, 5, 5), (4, 5, 3), (4, 6, 6), (5, 6, 1)])
        if not TRACK_PREVIOUS:
            self.assertEqual(g.dijkstra(1), [[0, 1], [1, 3], [2, 2],
                                             [3, 4], [4, 5], [5, 6]])
        else:
            self.assertEqual(
                g.dijkstra(1),
                [[0, 1], [1, 3, 1], [2, 2, 1], [3, 4, 2, 1], [4, 5, 2, 1],
                 [5, 6, 5, 2, 1]])
