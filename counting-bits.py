# counting bits
# https://neetcode.io/problems/counting-bits/question
# code by aveia@github

class Solution:
    def countBits(self, n: int) -> list[int]:
        r = []
        for i in range(0, n + 1):
            qty = 0
            while i != 0:
                qty += i % 2
                i //= 2
            r.append(qty)
        return r
