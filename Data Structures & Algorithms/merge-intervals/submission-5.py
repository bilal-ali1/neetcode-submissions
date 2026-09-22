class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        curr_interval = intervals[0]
        if len(intervals) == 1:
            return intervals
        for i in range(len(intervals) - 1):
            if curr_interval[1] < intervals[i + 1][0]:
                res.append(curr_interval)
                curr_interval = intervals[i + 1]
            else:        
                curr_interval = [min(curr_interval[0], intervals[i + 1][0]), max(curr_interval[1], intervals[i + 1][1])]
        res.append(curr_interval)
        return res