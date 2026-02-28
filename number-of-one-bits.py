# number of 1 bits
# https://neetcode.io/problems/number-of-one-bits/question
# code by aveia@github

class Solution:
    def hammingWeight(self, n: int) -> int:
        qty = 0
        while n != 0:
            qty += n % 2
            n //= 2
        return qty
