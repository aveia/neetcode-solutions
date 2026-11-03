# longest increasing path in matrix
# https://neetcode.io/problems/longest-increasing-path-in-matrix/question
# code by aveia@github

class Solution:
    def longestIncreasingPath(self, mtx: list[list[int]]) -> int:

        n, m = len(mtx), len(mtx[0])
        longest = [[None for _ in range(m)] for _ in range(n)]

        def larger(x, y, i, j):
            if not (0 <= x < n and 0 <= y < m):
                return False
            return mtx[x][y] > mtx[i][j]

        def neighbors(i, j):
            res = []
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if larger(x, y, i, j):
                    res.append((x, y))
            return res

        def dfs(i, j):
            nonlocal longest
            if longest[i][j] is not None:
                return longest[i][j]

            l = 1
            for x, y in neighbors(i, j):
                l = max(l, 1 + dfs(x, y))

            longest[i][j] = l
            return l

        for i in range(n):
            for j in range(m):
                dfs(i, j)

        mx = longest[0][0]
        for i in range(n):
            for j in range(m):
                mx = max(mx, longest[i][j])
        return mx
