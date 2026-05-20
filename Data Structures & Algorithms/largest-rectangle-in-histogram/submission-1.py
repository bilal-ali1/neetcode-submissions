class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stk:
                pidx, pheight = stk[-1]
                if height < pheight:
                    stk.pop()
                    start = pidx
                    area = (i - pidx) * pheight
                    maxArea = max(area, maxArea)
                else:
                    break
            stk.append((start, height))
            
        
        while stk:
            idx, h = stk.pop()
            area = (len(heights) - idx) * h
            maxArea = max(area, maxArea)
        
        return maxArea