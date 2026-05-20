class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if heaviest < second:
                heapq.heappush(stones, heaviest - second)
        
        print(stones)
        if stones:
            return (-1 * stones[-1])
        return 0