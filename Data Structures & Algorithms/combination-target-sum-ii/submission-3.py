class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        candidates = sorted(candidates)

        def backtrack(i, sum):
            if sum == target:
                res.append(sol.copy())
                return
            if sum > target or i >= len(candidates):
                return
            
            sol.append(candidates[i])
            backtrack(i + 1, sum + candidates[i])
            sol.pop()

            while i < len(candidates) - 1  and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, sum)
        
        backtrack(0, 0)
        return res
        