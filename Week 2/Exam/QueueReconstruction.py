import unittest


def reconstruct(queue):
    queue = sorted(queue)
    print(queue)

    queue.reverse()
    print(queue)

    for i in range(len(queue) - 1):
        if queue[i][0] == queue[i + 1][0] and queue[i][1] > queue[i + 1][1]:
            queue[i], queue[i + 1] = queue[i + 1], queue[i]
            i = 0

    print(queue)
    result = []
    for person in queue:
        result.insert(person[1], person)
    return result


class Test(unittest.TestCase):
    def test_one(self):
        queue = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        answer = reconstruct(queue)
        self.assertEqual(answer, expected)

    def test_two(self):
        queue = [[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]
        expected = [[12,0],[11,1],[9,2],[6,3],[3,4],[1,5]]
        answer = reconstruct(queue)
        self.assertEqual(answer, expected)

    def test_three(self):
        queue = [[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]
        expected = [[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]
        answer = reconstruct(queue)
        self.assertEqual(answer, expected)


unittest.main(verbosity=2)