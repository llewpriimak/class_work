import unittest
from example_022_minimum_spanning_tree_Kruskal_algo import Graph


class TestKruskalAlgorithm(unittest.TestCase):

    def setUp(self):
        self.g1 = Graph(7)
        self.g2 = Graph(5)
        self.graph_empty = Graph(0)
        self.graph_solo = {'Z'}


    def test_kruskal_mst(self):
        # Compute the minimum spanning tree using Kruskal's algorithm
        self.g1.add_edge(0, 1, 30)
        self.g1.add_edge(0, 6, 10)
        self.g1.add_edge(1, 4, 13)
        self.g1.add_edge(1, 2, 15)
        self.g1.add_edge(2, 3, 12)
        self.g1.add_edge(3, 4, 16)
        self.g1.add_edge(3, 5, 20)
        self.g1.add_edge(4, 5, 21)
        self.g1.add_edge(5, 6, 22)

        weight_total, edge_test = self.g1.kruskal_algo()
        # Assert that the total weight of the MST is correct
        self.assertEqual(92, weight_total)
        self.g2.add_edge(0, 1, 2)
        self.g2.add_edge(0, 2, 8)
        self.g2.add_edge(1, 2, 3)
        self.g2.add_edge(1, 4, 5)
        self.g2.add_edge(0, 3, 6)
        self.g2.add_edge(3, 4, 8)
        self.g2.add_edge(2, 3, 8)
        weight_total2, mst = self.g2.kruskal_algo()
        # Assert that the MST contains the correct edges
        expected_mst = [[0, 1, 2], [1, 2, 3], [1, 4, 5], [0, 3, 6]]
        self.assertEqual(mst, expected_mst)

    def test_kruskal_mst_empty_graph(self):

        weight_total, edge_test = self.graph_empty.kruskal_algo()

        # YOUR CODE 
        self.assertEqual(0, weight_total)
        self.assertEqual([], edge_test)

    def test_kruskal_mst_single_vertex(self):
        # Test with a graph with a single vertex
        # ...
        pass
        # YOUR CODE
        # self.assertEqual(   ,   )



    def test_kruskal_mst_disconnected_graph(self):
        # Test with a disconnected graph
        pass
        # ...

        # YOUR CODE
        # self.assertEqual(   ,   )

if __name__ == '__main__':
    unittest.main()
