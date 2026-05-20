class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # nlogn
        returnArray = []
        for index, num in enumerate(nums):
            if (index > 0) and (nums[index - 1] == num):
                continue
            l = index + 1
            r = len(nums) - 1
            while (l < r):
                if (num + nums[l] + nums[r]) == 0:
                    returnArray.append([num, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1]) and (l < r):
                        l += 1
                elif (num + nums[l] + nums[r]) > 0:
                    r -= 1
                else:
                    l += 1
        return returnArray

                



      
        

        