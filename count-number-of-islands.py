# number of islands
# https://neetcode.io/problems/count-number-of-islands/question
# code by aveia@github

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def flood(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            flood(i - 1, j)
            flood(i + 1, j)
            flood(i, j - 1)
            flood(i, j + 1)

        qty = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    qty += 1
                    flood(i, j)

        return qty
