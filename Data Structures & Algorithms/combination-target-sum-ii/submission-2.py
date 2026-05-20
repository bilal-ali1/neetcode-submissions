class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i, sum):
            if sum == target:
                if not(sorted(sol) in res):
                    res.append(sorted(sol))
                return
            if sum > target or i == len(candidates):
                return
            
            sol.append(candidates[i])
            backtrack(i + 1, sum + candidates[i])
            sol.pop()

            backtrack(i + 1, sum)
        
        backtrack(0, 0)
        return res
        