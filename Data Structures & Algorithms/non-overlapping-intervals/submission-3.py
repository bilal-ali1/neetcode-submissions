class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0]) # nlogn

        check = [intervals[0]]
        for i in range(1, len(intervals)):
            if check[-1][1] > intervals[i][0]: # overlap:
                check[-1][1] = min(intervals[i][1], check[-1][1])
            else: # no overlap
                check.append(intervals[i])
        print(check)
        return len(intervals) - len(check)
