
import unittest
from dag import has_cycle, find_cycle, top_sort

class TestDAGFunctions(unittest.TestCase):
    def test_acyclic(self):
        g = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
        self.assertFalse(has_cycle(g))
        self.assertIsNone(find_cycle(g))
        order = top_sort(g)
        self.assertCountEqual(order, ['A','B','C','D'])
        idx = {v: order.index(v) for v in order}
        self.assertLess(idx['A'], idx['B'])
        self.assertLess(idx['A'], idx['C'])
        self.assertLess(idx['B'], idx['D'])

    def test_simple_cycle(self):
        g = {'A': ['B'], 'B': ['C'], 'C': ['A']}
        self.assertTrue(has_cycle(g))
        cycle = find_cycle(g)
        self.assertIsNotNone(cycle)
        self.assertEqual(cycle[0], cycle[-1])
        self.assertSetEqual(set(cycle), {'A','B','C'})
        with self.assertRaises(ValueError):
            top_sort(g)

    def test_isolated_node(self):
        g = {'A':['B'], 'B':[], 'C':[]}
        self.assertFalse(has_cycle(g))
        self.assertIsNone(find_cycle(g))
        order = top_sort(g)
        self.assertCountEqual(order, ['A','B','C'])

    def test_disconnected_cycle(self):
        g = {'A':['B'], 'B':[], 'C':['D'], 'D':['C']}
        self.assertTrue(has_cycle(g))
        c = find_cycle(g)
        self.assertTrue('C' in c and 'D' in c)
        with self.assertRaises(ValueError):
            top_sort(g)

    def test_empty(self):
        g = {}
        self.assertFalse(has_cycle(g))
        self.assertIsNone(find_cycle(g))
        self.assertEqual(top_sort(g), [])

    def test_self_loop(self):
        g = {'A': ['A']}
        self.assertTrue(has_cycle(g))
        c = find_cycle(g)
        self.assertEqual(set(c), {'A'})
        self.assertEqual(c[0], c[-1])
        with self.assertRaises(ValueError):
            top_sort(g)

    def test_hole_key(self):
        g = {'A': ['B']} 
        self.assertFalse(has_cycle(g))
        self.assertIsNone(find_cycle(g))
        ts = top_sort(g)
        self.assertCountEqual(ts, ['A','B'])
        self.assertLess(ts.index('A'), ts.index('B'))

if __name__ == "__main__":
    unittest.main()