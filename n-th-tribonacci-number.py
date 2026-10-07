# n-th tribonacci number
# https://neetcode.io/problems/n-th-tribonacci-number/question
# code by aveia@github

# TODO: make it better

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return n and 1 or 0
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            c = a + b + c
            b = c - a - b
            a = c - b - a
        return c
