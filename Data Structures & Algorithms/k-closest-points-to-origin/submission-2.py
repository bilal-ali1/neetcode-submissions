class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        returnlist = []
        minheap = []
        for point in points:
            minheap.append([(point[0] * point[0] + point[1] * point[1]), point[0], point[1]])
        heapq.heapify(minheap)

        for i in range(k):
            point = heapq.heappop(minheap)
            returnlist.append(point[1:])
        
        return returnlist


        
        


        

        