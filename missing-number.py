# missing number
# https://neetcode.io/problems/missing-number/question
# code by aveia@github

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        k = len(nums)
        for i, x in enumerate(nums):
            k ^= x ^ i
        return k
