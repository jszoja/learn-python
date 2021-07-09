import unittest
import math
from game.astar.pathf import PathFinder, PathNode
from game.astar.Box import Box


class PathFinderTest(unittest.TestCase):

    def test_getNeighbours(self):
        map = []
        for row in range(3):
            map.append([Box(col, row, 20, map) for col in range(3)])
        self.assertEqual(1, map[2][1].x)
        self.assertEqual(2, map[2][1].y)

        self.assertEqual(math.sqrt(8), map[0][0].getDistance(map[2][2]))

        nbs = map[0][0].getNeighbours()
        self.assertEqual(2, len(nbs))
        self.assertEqual(0, nbs[0].x)
        self.assertEqual(1, nbs[0].y)
        self.assertEqual(1, nbs[1].x)
        self.assertEqual(0, nbs[1].y)

    def test_sqrt(self):
        self.assertEqual(4., math.sqrt(16))


if __name__ == '__main__':
    unittest.main()
