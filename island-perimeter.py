# island perimeter
# https://neetcode.io/problems/island-perimeter/question
# code by aveia@github

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        cells = 0
        edges = 0

        def count_adj(i, j):
            qty = 0
            qty += 1 * (0 <= i - 1 < len(grid) and grid[i - 1][j])
            qty += 1 * (0 <= i + 1 < len(grid) and grid[i + 1][j])
            qty += 1 * (0 <= j - 1 < len(grid[0]) and grid[i][j - 1])
            qty += 1 * (0 <= j + 1 < len(grid[0]) and grid[i][j + 1])
            return qty

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    cells += 1
                    edges += count_adj(i, j)

        return cells * 4 - edges
