# word search
# https://neetcode.io/problems/search-for-word/question
# code by aveia@github

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        n, m = len(board), len(board[0])

        word_letters = set(word)
        board_letters = set()
        for k in range(n * m):
            board_letters.add(board[k // m][k % m])

        if word_letters - board_letters:
            return False

        def neighbors(i, j):
            ns = []
            if i - 1 >= 0:
                ns.append([i - 1, j])
            if i + 1 < n:
                ns.append([i + 1, j])
            if j - 1 >= 0:
                ns.append([i, j - 1])
            if j + 1 < m:
                ns.append([i, j + 1])
            return ns

        def find(i, j, w, visited):
            if not w:
                return True
            if board[i][j] != w[0]:
                return False
            if not w[1:]:
                return True
            for a, b in neighbors(i, j):
                if (a, b) in visited:
                    continue
                if find(a, b, w[1:], visited | {(a, b)}):
                    return True
            return False

        for k in range(n * m):
            i, j = k // m, k % m
            if find(i, j, word, {(i, j)}):
                return True

        return False
