# concatenation of array
# https://neetcode.io/problems/concatenation-of-array/question
# code by aveia@github

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums_twice = []
        for i in range(2 * len(nums)):
            nums_twice.append(nums[i % len(nums)])
        return nums_twice
