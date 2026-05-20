class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, sum):
            if sum == target:
                if sol.copy() not in res:
                    res.append(sol.copy())
                return
            
            if i == len(nums) or sum > target:
                return

            # Add the current number, move forward:
            sol.append(nums[i])
            backtrack(i + 1, sum + nums[i])

            # add the current number, but don't move forward (duplicating):
            backtrack(i, sum + nums[i])

            sol.pop()

            # Don't add the current number, move forward:
            backtrack(i + 1, sum)
        
        backtrack(0, 0)
        return res
            

        