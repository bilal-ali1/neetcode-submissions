class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i] in dictionary) and not (dictionary[target - nums[i]] == i):
                return [i, dictionary[target - nums[i]]]

            