# majority element
# https://neetcode.io/problems/majority-element/question
# code by aveia@github

# TODO: O(1) space

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        from collections import defaultdict
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] > len(nums) // 2:
                return n
