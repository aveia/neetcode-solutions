# container with most water
# https://neetcode.io/problems/max-water-container/question
# code by aveia@github

class Solution:
    def maxArea(self, hs: list[int]) -> int:
        i, j = 0, len(hs) - 1
        max_h = 0
        while i < j:
            h = (j - i) * min(hs[i], hs[j])
            max_h = max(h, max_h)

            if hs[i] < hs[j]:
                i += 1
            else:
                j -= 1
        return max_h
