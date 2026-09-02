# surrounded regions
# https://neetcode.io/problems/surrounded-regions/question
# code by aveia@github

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        h, w = len(board), len(board[0])

        def bucket(l, c):
            nonlocal board
            if 0 <= l < h and 0 <= c < w and board[l][c] == 'O':
                board[l][c] = 'S'
                bucket(l - 1, c)
                bucket(l + 1, c)
                bucket(l, c - 1)
                bucket(l, c + 1)

        for l in range(h):
            bucket(l, 0)
            bucket(l, w - 1)
        for c in range(w):
            bucket(0, c)
            bucket(h - 1, c)

        for l in range(h):
            for c in range(w):
                board[l][c] = 'O' if board[l][c] == 'S' else 'X'
