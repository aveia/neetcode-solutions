# detect squares
# https://neetcode.io/problems/count-squares/question
# code by aveia@github

class CountSquares:

    def __init__(self):
        self.m = [[0] * 1001 for _ in range(1001)]

    def add(self, point: list[int]) -> None:
        x, y = point
        self.m[x][y] += 1

    def count(self, point: list[int]) -> int:
        m = self.m
        qty = 0
        x, y = point
        for i in range(1, 1001):
            for dx, dy in [(i, i), (i, -i), (-i, i), (-i, -i)]:
                if 0 <= x + dx < 1001 and 0 <= y + dy < 1001:
                    qty += m[x + dx][y] * m[x][y + dy] * m[x + dx][y + dy]
        return qty
