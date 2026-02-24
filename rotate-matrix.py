# rotate image
# https://neetcode.io/problems/rotate-matrix/question
# code by aveia@github

class Solution:
    def rotate(self, m: list[list[int]]) -> None:
        n = len(m)

        # transpose
        for i in range(n):
            for j in range(i + 1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]

        # flip horizontally
        for i in range(n):
            for j in range(n // 2):
                m[i][j], m[i][n - j - 1] = m[i][n - j - 1], m[i][j]
