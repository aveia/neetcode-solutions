# meeting rooms
# https://neetcode.io/problems/meeting-schedule/question
# code by aveia@github

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:

        def conflict(i1, i2):
            if i1.start >= i2.end:
                return False
            if i2.start >= i1.end:
                return False
            return True

        intervals = sorted(intervals, key=lambda i: (i.start, i.end))

        for j in range(len(intervals) - 1):
            if conflict(intervals[j], intervals[j + 1]):
                return False
        return True
