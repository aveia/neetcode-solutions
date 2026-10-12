# remove duplicates from sorted array
# https://neetcode.io/problems/remove-duplicates-from-sorted-array/question
# code by aveia@github

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, j = 0, 0
        prev = None
        for i, n in enumerate(nums):
            if n != prev:
                prev = nums[j] = n
                j += 1
        return j
