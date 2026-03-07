# valid sudoku
# https://neetcode.io/problems/valid-sudoku/question
# code by aveia@github

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            nums_ij = set()
            nums_ji = set()
            nums_sq = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in nums_ij:
                        return False
                    nums_ij.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in nums_ji:
                        return False
                    nums_ji.add(board[j][i])
                l = i // 3 * 3 + j // 3
                c = i  % 3 * 3 + j  % 3
                if board[l][c] != '.':
                    if board[l][c] in nums_sq:
                        return False
                    nums_sq.add(board[l][c])
        return True
