# merge intervals
# https://neetcode.io/problems/merge-intervals/question
# code by aveia@github

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals)
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            cur, prev = intervals[i], out[-1]
            if cur[0] <= prev[1]:
                out[-1] = [min(cur[0], prev[0]), max(cur[1], prev[1])]
            else:
                out.append(cur)
        return out
