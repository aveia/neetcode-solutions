# spiral matrix
# https://neetcode.io/problems/spiral-matrix/question
# code by aveia@github

class Solution:
    def spiralOrder(self, mtx: list[list[int]]) -> list[int]:
        res = []
        l, c = 0, -1
        step = 1
        h, w = len(mtx) - 1, len(mtx[0])
        while w:
            for _ in range(w):
                c += step
                res.append(mtx[l][c])
            if not h:
                break
            for _ in range(h):
                l += step
                res.append(mtx[l][c])
            step = -step
            w, h = w - 1, h - 1
        return res
