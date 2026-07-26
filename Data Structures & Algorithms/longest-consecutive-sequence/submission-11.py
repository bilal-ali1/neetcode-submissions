class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)
        for num in numSet:
            if not num - 1 in numSet:
                search = num + 1
                lenSub = 1
                while search in numSet:
                    lenSub += 1
                    search += 1
                maxLen = max(maxLen, lenSub)
        return maxLen 
        
        