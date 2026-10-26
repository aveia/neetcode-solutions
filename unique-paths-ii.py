# unique paths ii
# https://neetcode.io/problems/unique-paths-ii/question
# code by aveia@github

class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        unique = [[0 for _ in range(m)] for _ in range(n)]
        unique[n - 1][m - 1] = 1 - grid[n - 1][m - 1]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if unique[i][j]:
                    continue
                ways = 0
                if i + 1 < n:
                    ways += unique[i + 1][j]
                if j + 1 < m:
                    ways += unique[i][j + 1]
                unique[i][j] = (1 - grid[i][j]) * ways

        return unique[0][0]
