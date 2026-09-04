# unique paths
# https://neetcode.io/problems/count-paths/question
# code by aveia@github

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mtx = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            mtx[i][n - 1] = 1
        for i in range(n):
            mtx[m - 1][i] = 1

        for l in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                mtx[l][c] = mtx[l + 1][c] + mtx[l][c + 1]

        return mtx[0][0]
