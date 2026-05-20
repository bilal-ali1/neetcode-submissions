class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            minheap.append(num)
        
        heapq.heapify(minheap)
        
        while (len(minheap) > k):
            heapq.heappop(minheap)
        
        if minheap:
            return minheap[0]
        return -1


        