
import unittest
from dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test_simple(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1},
        }
        res = dijkstra(graph, 'A')
        self.assertEqual(res, {'A': 0, 'B': 1, 'C': 3, 'D': 4})

    def test_unreachable(self):
        graph = {
            1: {2: 7},
            2: {},
            3: {4: 1},
            4: {}
        }
        res = dijkstra(graph, 1)
        # 1 до 1: 0, до 2: 7, до остальных: inf
        self.assertEqual(res[1], 0)
        self.assertEqual(res[2], 7)
        self.assertEqual(res[3], float('inf'))
        self.assertEqual(res[4], float('inf'))

    def test_loop(self):
        graph = {
            'X': {'X': 2, 'Y': 1},
            'Y': {'X': 1}
        }
        res = dijkstra(graph, 'X')
        self.assertEqual(res, {'X': 0, 'Y': 1})
        res2 = dijkstra(graph, 'Y')
        self.assertEqual(res2, {'Y': 0, 'X': 1})

    def test_single_node(self):
        graph = {42: {}}
        res = dijkstra(graph, 42)
        self.assertEqual(res, {42:0})

    def test_empty(self):
        res = dijkstra({}, 1)
        self.assertEqual(res, {1: 0})

    def test_disconnected_key_not_in_graph(self):
        graph = {1: {2: 1}, 2: {}, 4: {}}
        res = dijkstra(graph, 3)
        self.assertEqual(res, {1:float('inf'), 2:float('inf'), 4:float('inf'), 3:0})

    def test_zero_weight(self):
        graph = {
            1: {2: 0, 3: 2},
            2: {3: 0},
            3: {}
        }
        res = dijkstra(graph, 1)
        self.assertEqual(res, {1:0, 2:0, 3:0})

if __name__ == "__main__":
    unittest.main()