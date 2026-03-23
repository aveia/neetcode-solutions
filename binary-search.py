# binary search
# https://neetcode.io/problems/binary-search/question
# code by aveia@github

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        return -1
