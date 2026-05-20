class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(k):
            minHeap.append(nums[i])
        
        heapq.heapify(minHeap)

        for i in range(k, len(nums)):
            heapq.heappush(minHeap, nums[i])
            while len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]