class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heapify the stones weights:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if (largest < second):
                largest = largest - second
                heapq.heappush(stones, largest)
        
        if stones:
            return -1 * stones[0]
        return 0
            
            