class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res, subsets = [], []

        def backtrack(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # Add the number:
            subsets.append(nums[i])
            backtrack(i + 1)
            subsets.pop()


            # dont add the number (AT ALL SKIP IT ALL TOGETHER):
            while i < len(nums) - 1 and (nums[i + 1] == nums[i]):
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return res