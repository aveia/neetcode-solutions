# subsets
# https://neetcode.io/problems/subsets/question
# code by aveia@github

# TODO: solve using stack

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        perms = []
        for k in range(2 ** n):
            perms.append([nums[i] for i in range(n) if k & (2 ** i)])
        return perms
