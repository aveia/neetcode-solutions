# 3sum
# https://neetcode.io/problems/three-integer-sum/question
# code by aveia@github

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        from collections import defaultdict
        cs = defaultdict(list)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                cs[0 - nums[i] - nums[j]].append([i, j])

        out = set()
        for i, n in enumerate(nums):
            if n in cs:
                for pair in cs[n]:
                    if i not in pair:
                        out.add(tuple(sorted(list(map(lambda i: nums[i], pair)) + [n])))
        return list(list(x) for x in out)
