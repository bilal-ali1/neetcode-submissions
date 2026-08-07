class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        i = 0
        while i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l - 1] == nums[l]:
                        l += 1
                elif (nums[i] + nums[l] + nums[r] > 0):
                    r -= 1
                else:
                    l += 1
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
        return ans