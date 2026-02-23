# two sum
# https://neetcode.io/problems/two-integer-sum/question
# code by aveia@github

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cs = {}
        for i, n in enumerate(nums):
            c = target - n
            if n in cs and i != cs[n]:
                return sorted([i, cs[n]])
            cs[c] = i
