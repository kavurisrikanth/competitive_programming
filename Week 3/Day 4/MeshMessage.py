import unittest


def bfs_get_path(graph, start_node, end_node):
    # Find the shortest route in the network between the two users

    if start_node not in graph or end_node not in graph:
        raise KeyError('Nodes are not in the graph!')

    if start_node == end_node:
        return [start_node]

    next_nodes = [start_node]
    done = False

    visited = {}
    order = []

    for node in graph:
        visited[node] = False

    while len(next_nodes) > 0 and not done:
        current_node = next_nodes.pop(0)
        if not visited[current_node]:
            visited[current_node] = True
            order.append(current_node)

            if end_node in graph[current_node]:
                order.append(end_node)
                done = True
            else:
                if current_node != start_node:
                    order.remove(current_node)
                next_nodes = next_nodes + graph[current_node]

    if not done:
        return None

    return order


# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)