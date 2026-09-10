class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(i, lst):
            if sum(lst) > target:
                return
            if i >= len(nums):
                if sum(lst) == target:
                    ret.append(lst.copy())
                    return
                return

            # Don't take the current
            backtrack(i + 1, lst)
            lst.append(nums[i])
            backtrack(i, lst)
            lst.pop()
        
        backtrack(0, [])
        return ret