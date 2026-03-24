# single number
# https://neetcode.io/problems/single-number/question
# code by aveia@github

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        k = 0
        for x in nums:
            k ^= x
        return k
