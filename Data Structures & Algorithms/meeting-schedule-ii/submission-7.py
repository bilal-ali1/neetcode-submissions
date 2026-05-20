"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        maxCount = 0
        count = 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
                maxCount = max(maxCount, count)
            else:
                j += 1
                count -= 1
        
        return maxCount