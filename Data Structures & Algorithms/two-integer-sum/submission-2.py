class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in sumDict:
                return [sumDict[need], i]
            sumDict[nums[i]] = i
        