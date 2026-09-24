class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda i : i[0])
        meetingCount = [0] * n
        available = [i for i in range(n)] # all available to start
        used = [] # empty to start, [end time, room #]

        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            # if no room is available, remove next room from used, add it back with new end
            if not available:
                endTime, room = heapq.heappop(used)
                meetingCount[room] += 1
                newEnd = endTime + (end - start)
                heapq.heappush(used, [newEnd, room])
            # if room is availabe, remove it and add it to used
            else:
                room = heapq.heappop(available)
                meetingCount[room] += 1
                heapq.heappush(used, [end, room])
        
        return meetingCount.index(max(meetingCount))



    




