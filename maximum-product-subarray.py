# maximum product subarray
# https://neetcode.io/problems/maximum-product-subarray/question
# code by aveia@github

class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        prev_max = prev_min = nums[0]
        the_max = prev_max

        for i in range(1, len(nums)):
            mul_prev_max = nums[i] * prev_max
            mul_prev_min = nums[i] * prev_min
            prev_max = max(nums[i], mul_prev_max, mul_prev_min)
            prev_min = min(nums[i], mul_prev_max, mul_prev_min)
            the_max = max(the_max, prev_max)

        return the_max
