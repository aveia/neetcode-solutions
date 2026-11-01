# spiral matrix
# https://neetcode.io/problems/spiral-matrix/question
# code by aveia@github

class Solution:
    # def spiralOrder(self, mtx: list[list[int]]) -> list[int]:
    #     res = []
    #     l, c = 0, -1
    #     step = 1
    #     h, w = len(mtx) - 1, len(mtx[0])
    #     while w:
    #         for _ in range(w):
    #             c += step
    #             res.append(mtx[l][c])
    #         if not h:
    #             break
    #         for _ in range(h):
    #             l += step
    #             res.append(mtx[l][c])
    #         step = -step
    #         w, h = w - 1, h - 1
    #     return res

    def spiralOrder(self, mtx: list[list[int]]) -> list[int]:
        n, m = len(mtx[0]), len(mtx) - 1
        i, j = (0, -1)
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        si = 0
        res = []
        while n:
            for _ in range(n):
                i, j = i + steps[si % 4][0], j + steps[si % 4][1]
                res.append(mtx[i][j])
            n, m = m, n - 1
            si += 1
        return res
