class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while r >= l:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break   
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])
            if nums[r] >= nums[mid]: # we are in the right sorted portion
                r = mid - 1
            elif nums[l] <= nums[mid]: # we are in the left sorted portion
                l = mid + 1   
        return minimum