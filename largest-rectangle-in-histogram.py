# largest rectangle in histogram
# https://neetcode.io/problems/largest-rectangle-in-histogram/question
# code by aveia@github

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []
        max_rect = 0

        for i, h in enumerate(heights):

            top_i, top_h = None, None

            while stack and h <= stack[-1][1]:
                top_i, top_h = stack.pop()
                max_rect = max(max_rect, (i - top_i) * top_h)

            stack.append((i if top_i is None else top_i, h))

        while stack:
            top_i, top_h = stack.pop()
            max_rect = max(max_rect, (len(heights) - top_i) * top_h)

        return max_rect
