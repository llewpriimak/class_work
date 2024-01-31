import unittest
from typing import List, Tuple
from example_023_minimum_spanning_tree_Prims_algo import Graph

class TestPrimsAlgorithm(unittest.TestCase):
    
    def setUp(self):
        self.graph1 = {
            'A': [('B', 2), ('C', 3)],
            'B': [('A', 2), ('C', 4), ('D', 1)],
            'C': [('A', 3), ('B', 4), ('D', 2)],
            'D': [('B', 1), ('C', 2)]
        }
        self.expected_output1 = [('A', 'B', 2), ('B', 'D', 1), ('D', 'C', 2)]

        # Create your Test Graphs here.
        self.test_graph1 = Graph()
        self.test_graph1.add_verticies(range(4))
        self.test_graph1.add_undirected_edge(0, 1, 2)
        self.test_graph1.add_undirected_edge(0, 2, 3)
        self.test_graph1.add_undirected_edge(1, 2, 4)
        self.test_graph1.add_undirected_edge(1, 3, 1)
        self.test_graph1.add_undirected_edge(2, 3, 2)
        # YOUR CODE
        self.g2 = Graph()

    
    def test_prims_algorithm_with_graph1(self):

        expected_mst = [[0, 1, 2], [1, 3, 1], [3, 2, 2]]
        # YOUR CODE
        self.assertEqual(expected_mst, self.test_graph1.prims())
        
    def test_prims_algorithm_with_graph2(self):
        # ...
        self.g2.add_verticies(range(7))

        self.g2.add_undirected_edge(0, 1, 30)
        self.g2.add_undirected_edge(0, 6, 10)
        self.g2.add_undirected_edge(1, 4, 13)
        self.g2.add_undirected_edge(1, 2, 15)
        self.g2.add_undirected_edge(2, 3, 12)
        self.g2.add_undirected_edge(3, 4, 16)
        self.g2.add_undirected_edge(3, 5, 20)
        self.g2.add_undirected_edge(4, 5, 21)
        self.g2.add_undirected_edge(5, 6, 22)
        expected_mst = [[0, 6, 10], [6, 5, 22], [5, 3, 20], [3, 2, 12], [2, 1, 15], [1, 4, 13]]
        self.assertEqual(expected_mst, self.g2.prims())

    def test_prims_algorithm_with_graph3(self):
        # ...
        pass
        # YOUR CODE
        # self.assertEqual(   ,   )

if __name__ == '__main__':
    unittest.main()
