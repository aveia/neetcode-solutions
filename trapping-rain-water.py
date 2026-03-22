# trapping rain water
# https://neetcode.io/problems/trapping-rain-water/question
# code by aveia@github

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        filled = [0 for _ in height]
        max_h = 0
        for i in range(n):
            max_h = max(height[i], max_h)
            filled[i] = max_h
        max_h = 0
        for i in range(n):
            max_h = max(height[n - i - 1], max_h)
            filled[n - i - 1] = min(filled[n - i - 1], max_h)
        return sum(filled) - sum(height)
