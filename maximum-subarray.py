# maximum subarray
# https://neetcode.io/problems/maximum-subarray/question
# code by aveia@github

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m = nums[0]
        s = 0
        for x in nums:
            if s < 0:
                s = 0
            s += x
            m = max(s, m)
        return m
