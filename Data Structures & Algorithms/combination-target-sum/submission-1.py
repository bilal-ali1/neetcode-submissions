class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, sum):
            if sum == target:
                if not sol in res:
                    res.append(sol.copy())

            if sum > target:
                return

            if i >= len(nums):
                return

            # use the number again:
            sol.append(nums[i])
            backtrack(i, sum + nums[i])
            sol.pop()
            # add the number:
            backtrack(i + 1, sum)

        backtrack(0, 0) 
        return res