class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) ## O(n)
        ret = []
        i = 0
        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[r] + nums[l] < (0 - nums[i]):
                    l += 1
                elif nums[r] + nums[l] > (0 - nums[i]):
                    r -= 1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and (nums[l] == nums[l - 1]):
                        l += 1
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
        return ret