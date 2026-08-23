class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = 0
        while l < len(nums) - 1:
            if nums[l + 1] < nums[l]:
                # Do binary search to find optimal location
                toInsert = nums.pop(l + 1)
                left, right = 0, l
                while left <= right:
                    m = (left + right) // 2
                    if toInsert < nums[m]:
                        right = m - 1
                    else:
                        left = m + 1
                nums.insert(left, toInsert)
            l += 1
        return nums