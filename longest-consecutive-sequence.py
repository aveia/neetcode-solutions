# longest consecutive sequence
# https://neetcode.io/problems/longest-consecutive-sequence/question
# code by aveia@github

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            longest = max(current, longest)

        return longest
