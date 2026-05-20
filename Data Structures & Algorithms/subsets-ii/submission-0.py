class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res, sol = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(sol.copy())
                return
            
            # add the number and move forward:
            sol.append(nums[i])
            backtrack(i + 1)

            # Dont add the number and move forwards
            sol.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res

            