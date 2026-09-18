# remove element
# https://neetcode.io/problems/remove-element/question
# code by aveia@github

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        shift = 0
        for i in range(len(nums)):
            if nums[i] == val:
                shift += 1
            else:
                nums[i - shift] = nums[i]
        return len(nums) - shift
