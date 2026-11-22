# combinations
# https://neetcode.io/problems/combinations/question
# code by aveia@github

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:

        def combs(i, n, k):
            if k == 1:
                return [[c] for c in range(i, n + 1)]

            res = []
            for c in range(i, n + 1):
                for comb in combs(c + 1, n, k - 1):
                    res.append([c] + comb)
            return res

        return combs(1, n, k)
