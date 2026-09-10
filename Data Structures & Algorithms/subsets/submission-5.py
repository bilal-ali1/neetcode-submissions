class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(i, lst):
            if i >= len(nums):
                ret.append(lst.copy())
                return
            backtrack(i + 1, lst)
            lst.append(nums[i])
            backtrack(i + 1, lst)
            lst.pop()
        backtrack(0, [])
        return ret