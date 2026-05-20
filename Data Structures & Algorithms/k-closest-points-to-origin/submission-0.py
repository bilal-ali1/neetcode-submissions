class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # want to return the k nearest points: minHeap
        minheap = []
        return_list = []
        for point in points:
            dist = (point[0] * point[0]) + (point[1] * point[1])
            minheap.append([dist, point[0], point[1]])
        
        heapq.heapify(minheap)
        
        for i in range(k):
            ithPoint = heapq.heappop(minheap)
            return_list.append(ithPoint[1:])
        
        return return_list
        
        


        

        