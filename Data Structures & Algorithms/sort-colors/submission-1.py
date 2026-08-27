class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqDict = {}
        freqDict[0] = 0
        freqDict[1] = 0
        freqDict[2] = 0

        for num in nums:
            freqDict[num] += 1
        
        i = 0
        while i < len(nums):
            for key in freqDict.keys():
                for k in range(freqDict[key]):
                    nums[i] = key
                    i += 1
        return nums