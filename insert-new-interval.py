# insert interval
# https://neetcode.io/problems/insert-new-interval/question
# code by aveia@github

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        def overlap(i1, i2):
            i1, i2 = sorted([i1, i2])
            return i1[1] >= i2[0]

        def merge(i1, i2):
            return [min(i1[0], i2[0]), max(i1[1], i2[1])]

        intervals.extend([None])
        n = len(intervals)
        for k in range(n):
            intervals[n - k - 1] = intervals[n - k - 2]
        intervals[0] = None

        i, j = 1, -1
        inserted_new = False

        while i < n:
            if overlap(intervals[i], newInterval):
                newInterval = merge(intervals[i], newInterval)
                if j >= 0 and intervals[j] is not None \
                        and overlap(intervals[j], newInterval):
                    intervals[j] = merge(intervals[j], newInterval)
                else:
                    j += 1
                    intervals[j] = newInterval
                i += 1
                inserted_new = True
                break
            elif newInterval <= intervals[i]:
                j += 1
                intervals[j] = newInterval
                inserted_new = True
                break
            else:
                j += 1
                intervals[j] = intervals[i]
                i += 1

        while i < n:
            if j >= 0 and intervals[j] is not None and overlap(intervals[j], intervals[i]):
                intervals[j] = merge(intervals[j], intervals[i])
            else:
                j += 1
                intervals[j] = intervals[i]
            i += 1

        if not inserted_new:
            j += 1
            intervals[j] = newInterval

        del intervals[j + 1:]
        return intervals
