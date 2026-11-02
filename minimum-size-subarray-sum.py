# minimum size subarray sum
# https://neetcode.io/problems/minimum-size-subarray-sum/question
# code by aveia@github

# TODO: understand why it can't loop forever

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        mn = None
        s = 0
        while i < n or j < n:
            if s < target and j < n:
                s += nums[j]
                j += 1
            elif i < j:
                s -= nums[i]
                i += 1
            if s >= target and (mn is None or j - i < mn):
                mn = j - i

        return 0 if mn is None else mn
