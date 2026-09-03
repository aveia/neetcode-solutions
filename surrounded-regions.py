# surrounded regions
# https://neetcode.io/problems/surrounded-regions/question
# code by aveia@github

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        lines, columns = len(board), len(board[0])

        def bucket(l, c):
            nonlocal board
            if 0 <= l < lines and 0 <= c < columns and board[l][c] == 'O':
                board[l][c] = 'S'
                bucket(l - 1, c)
                bucket(l + 1, c)
                bucket(l, c - 1)
                bucket(l, c + 1)

        for l in range(lines):
            bucket(l, 0)
            bucket(l, columns - 1)
        for c in range(1, columns - 1): # skip first and last columns
            bucket(0, c)
            bucket(lines - 1, c)

        for l in range(lines):
            for c in range(columns):
                board[l][c] = 'O' if board[l][c] == 'S' else 'X'
