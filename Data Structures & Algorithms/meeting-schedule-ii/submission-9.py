"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i : i.start)
        rooms = []
        rooms_needed = 0
        if intervals:
            rooms_needed = 1
            rooms.append(intervals[0].end)
            heapq.heapify(rooms)
            for interval in intervals[1:]:
                next_available = rooms[0]
                if next_available > interval.start:
                    rooms_needed += 1
                else: # next available room can work
                    heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)
        return rooms_needed
