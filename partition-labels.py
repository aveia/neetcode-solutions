# partition labels
# https://neetcode.io/problems/partition-labels/question
# code by aveia@github

class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        intervals = {}
        for i, c in enumerate(s):
            if c in intervals:
                begin, end = intervals[c]
                intervals[c] = (min(begin, i), max(end, i))
            else:
                intervals[c] = (i, i)

        intervals = sorted(intervals.values())

        merged = [intervals[0]]
        for begin, end in intervals[1:]:
            prev_begin, prev_end = merged[-1]
            if begin <= prev_end:
                merged[-1] = (min(begin, prev_begin), max(end, prev_end))
            else:
                merged.append((begin, end))

        return [end - begin + 1 for begin, end in merged]
