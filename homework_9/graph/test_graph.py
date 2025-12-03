
import unittest
from graph import find_connected_components

class TestConnectedComponents(unittest.TestCase):
    def check_components(self, actual, expected):
        ac = {frozenset(c) for c in actual}
        ex = {frozenset(c) for c in expected}
        self.assertEqual(ac, ex)

    def test_empty(self):
        empty = {}
        self.assertEqual(find_connected_components(empty), [])

    def test_one_node(self):
        one_node = {1: []}
        self.assertEqual(find_connected_components(one_node), [[1]])

    def test_two_isolated(self):
        two_isolated = {1: [], 2: []}
        res = find_connected_components(two_isolated)
        self.check_components(res, [[1],[2]])

    def test_chain(self):
        chain = {1: [2], 2: [1, 3], 3: [2]}
        res = find_connected_components(chain)
        self.check_components(res, [[1,2,3]])

    def test_two_components(self):
        two_comps = {1: [2], 2: [1], 3: []}
        res = find_connected_components(two_comps)
        self.check_components(res, [[1,2],[3]])

    def test_loop(self):
        loop = {1: [1]}
        res = find_connected_components(loop)
        self.check_components(res, [[1]])

    def test_missing_key(self):
        missing_key = {1: [2, 3]}
        res = find_connected_components(missing_key)
        self.check_components(res, [[1,2,3]])

    def test_unidirect(self):
        unidirect = {1: [2], 2: []}
        res = find_connected_components(unidirect)
        self.check_components(res, [[1,2]])

    def test_big_connected(self):
        big_conn = {i: [i+1] for i in range(1, 1000)}
        big_conn[1000] = []
        res = find_connected_components(big_conn)
        self.check_components(res, [list(range(1,1001))])

if __name__ == "__main__":
    unittest.main()