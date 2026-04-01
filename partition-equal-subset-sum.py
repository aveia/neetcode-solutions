# partition equal subset sum
# https://neetcode.io/problems/partition-equal-subset-sum/question
# code by aveia@github

class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        if not nums:
            return True

        s = sum(nums)
        if s % 2:
            return False
        target = s // 2

        memo = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if num < target:
                memo[i][num] = True
            else:
                return False
            for t in range(target + 1):
                if memo[i - 1][t]:
                    memo[i][t] = True
                    if t + num < target:
                        memo[i][t + num] = True

        return memo[len(nums) - 1][target]
