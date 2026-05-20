class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for h in height]
        postfix = [0 for h in height]
        area = 0

        # Setting up prefix array:
        for i in range(1, len(height)):
            prefix[i] = max(height[:i])
        
        # Setting up postfix array:
        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(height[i : len(height)])
        
        for i in range(len(height)):
            idxArea = min(postfix[i], prefix[i]) - height[i]
            if idxArea > 0:
                area += idxArea
        
        return area