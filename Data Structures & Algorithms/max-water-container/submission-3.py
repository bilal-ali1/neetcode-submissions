class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        maxArea = (r - l) * min(heights[l], heights[r])
        while (l < r):
            if (heights[r] > heights[l]):
                l += 1
            else:
                r -= 1
            area = (r - l) * min(heights[l], heights[r])
            maxArea = max(area, maxArea)

        return maxArea

            
            


            
        

            
        