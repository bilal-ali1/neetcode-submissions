class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        longest = 0
        for num in nums:
            length = 1
            while (num + length) in nums:
                length += 1
            longest = max(longest, length)
        
        return longest