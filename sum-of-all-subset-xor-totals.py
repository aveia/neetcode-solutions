# sum of all subsets xor total
# https://neetcode.io/problems/sum-of-all-subset-xor-totals/question
# code by aveia@github

# TODO: improve it if possible

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        s = 0
        for i in range(2 ** len(nums)):
            k = 0
            for j, n in enumerate(nums):
                k ^= n if i & 2 ** j else 0
            s += k
        return s
