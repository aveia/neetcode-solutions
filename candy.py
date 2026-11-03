# candy
# https://neetcode.io/problems/candy/question
# code by aveia@github

class Solution:
    def candy(self, ratings: list[int]) -> int:

        n = len(ratings)
        qty = [None] * n

        def worse_rated_neighbors(i):
            res = []
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                res.append(i - 1)
            if i + 1 < n and ratings[i] > ratings[i + 1]:
                res.append(i + 1)
            return res

        def dfs(i):
            nonlocal qty
            if qty[i] is not None:
                return qty[i]

            q = 1
            for j in worse_rated_neighbors(i):
                q = max(q, 1 + dfs(j))

            qty[i] = q
            return q

        for i in range(n):
            dfs(i)

        return sum(qty)
