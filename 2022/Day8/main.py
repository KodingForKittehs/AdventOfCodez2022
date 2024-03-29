import unittest
import pathlib

input_file = f"{pathlib.Path(__file__).parent}/input.txt"

heights = []
visible = []

dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

with open(input_file) as file:
    for line in file.readlines():
        line = line.strip()
        heights.append([int(h) for h in line])
        visible.append([False for h in line])
h = len(heights)
w = len(heights[0])


def in_bounds(i, j):
    return i >= 0 and i < h and j >= 0 and j < w


def get_scenic(i, j):
    res = []
    th = heights[i][j]
    for dir in dirs:
        ii = i + dir[0]
        jj = j + dir[1]
        dist = 0
        while in_bounds(ii, jj):
            hij = heights[ii][jj]
            if hij < th:
                dist += 1
            if hij >= th:
                dist += 1
                break
            ii = ii + dir[0]
            jj = jj + dir[1]
        res.append(dist)
    return res[0] * res[1] * res[2] * res[3]


def problem():
    scenic_max = 0

    for i in range(h):
        mx = -1
        for j in range(w):
            if heights[i][j] > mx:
                mx = heights[i][j]
                visible[i][j] = True
        mx = -1
        for j in range(w - 1, -1, -1):
            if heights[i][j] > mx:
                mx = heights[i][j]
                visible[i][j] = True

    for j in range(w):
        mx = -1
        for i in range(h):
            if heights[i][j] > mx:
                mx = heights[i][j]
                visible[i][j] = True
        mx = -1
        for i in range(h - 1, -1, -1):
            if heights[i][j] > mx:
                mx = heights[i][j]
                visible[i][j] = True

    sum = 0
    for i in range(h):
        for j in range(w):
            if visible[i][j]:
                sum += 1
            scenic_max = max(
                scenic_max,
                get_scenic(i, j))

    return sum, scenic_max


class ProblemTestCase(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem()[0], 1669)

    def test_problem2(self):
        self.assertEqual(problem()[1], 331344)


if __name__ == '__main__':
    unittest.main()
