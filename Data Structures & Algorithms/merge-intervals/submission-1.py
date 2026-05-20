class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) # nlogn
        if not intervals:
            return intervals
        # res = []
        def mergeInterval(newInterval, restIntervals):
            if len(restIntervals) == 0:
                return [newInterval]
            # new interval does not overlap with first in rest
            if newInterval[1] < restIntervals[0][0]:
                return [newInterval] + mergeInterval(restIntervals[0], restIntervals[1:])
        
            # new interval overlaps with first in rest
            newInterval = [
                min(newInterval[0], restIntervals[0][0]), 
                max(newInterval[1], restIntervals[0][1])
            ]
            return mergeInterval(newInterval, restIntervals[1:])
        
        return mergeInterval(intervals[0], intervals[1:])