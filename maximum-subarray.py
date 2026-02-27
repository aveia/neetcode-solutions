# maximum subarray
# https://neetcode.io/problems/maximum-subarray/question
# code by aveia@github

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m = nums[0]
        s = 0
        for x in nums:
            s += x
            if s > m:
                m = s
            if s < 0:
                s = 0
        return m
