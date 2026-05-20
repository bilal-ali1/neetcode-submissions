class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or sum(subset) > target:
                return

            subset.append(nums[i])
            backtrack(i)

            subset.pop()
            backtrack(i + 1)
            

        
        backtrack(0)
        return res

