class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removals = 0
        intervals.sort(key = lambda i : i[0])
        curr_interval = intervals[0]
        for i in range(len(intervals) - 1):
            # no overlap:
            if curr_interval[1] <= intervals[i + 1][0]:
                curr_interval = intervals[i + 1]
            # there is an overlap
            else:
                removals += 1
                if intervals[i + 1][1] < curr_interval[1]:
                    curr_interval = intervals[i + 1]
                # otherwise keep curr_intervals the same and move forward
        return removals

