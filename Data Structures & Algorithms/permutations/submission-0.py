class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        possiblePerms = self.permute(nums[1:])
        for perm in possiblePerms:
            for k in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(k, nums[0])
                res.append(perm_copy)
        return res
        
        return res