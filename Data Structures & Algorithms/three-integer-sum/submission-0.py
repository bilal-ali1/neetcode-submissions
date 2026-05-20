class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if the first two pointers add up to necessary val for third pointer
        # if greater, then sub from right pointer
        # if less then add to left pointer
        # if l = r and no solution, then decrement right most pointer, and reset l anr r pointers
        nums = sorted(nums) # nlogn time
        l = 0
        r = len(nums) - 1
        m = r - 1
        returnList = []
        for index, num in enumerate(nums):
            if index > 0 and (num == nums[index - 1]):
                continue
            l = index + 1
            r = len(nums) - 1
            target = 0 - num
            while l < r:
                if (nums[l] + nums[r] == target):
                    returnList.append([num, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1]) and l < r:
                        l += 1
                elif (nums[l] + nums[r] > target):
                    r -= 1
                elif (nums[l] + nums[r] < target):
                    l += 1
        return returnList



      
        

        