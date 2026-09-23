"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meeting_list = []
        for interval in intervals:
            meeting_list.append([interval.start, interval.end])
        meeting_list.sort(key = lambda i : i[0])
        if meeting_list:
            curr_meeting = meeting_list[0]
            for meeting in meeting_list[1:]:
                if curr_meeting[1] <= meeting[0]:
                    curr_meeting = meeting
                else:
                    return False
        return True
