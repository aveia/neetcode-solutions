# search a 2d matrix
# https://neetcode.io/problems/search-2d-matrix/question
# code by aveia@github

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, rows * cols - 1
        while i <= j:
            m = (i + j) // 2
            a, b = m // cols, m % cols
            if target < matrix[a][b]:
                j = m - 1
            elif target > matrix[a][b]:
                i = m + 1
            else:
                return True
        return False
