class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if (largest < second):
                heapq.heappush(stones, largest - second)
        if (len(stones) == 1):
            return abs(stones[0])
        else:
            return 0
            