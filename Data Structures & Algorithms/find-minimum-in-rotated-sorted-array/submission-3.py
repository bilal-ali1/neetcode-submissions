class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            curr = (l + r) // 2
            minimum = min(minimum, nums[curr])
            if nums[curr] >= nums[l]:
                l = curr + 1
            else:
                r = curr - 1
        return minimum