class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = -1
        l, r = 0, len(nums) - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] == target:
                found = m
                break
            if nums[l] <= nums[m]: # we are in the left sorted portion
                if nums[l] <= target and nums[m] > target: # move left
                    r = m - 1
                else: # move right
                    l = m + 1
            else: # we are in the right sorted portion
                if nums[r] >= target and nums[m] < target: # move left
                    l = m + 1
                else: # move right
                    r = m - 1
                    
        return found