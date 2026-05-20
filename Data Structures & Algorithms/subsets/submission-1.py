class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for num in nums:
            newsubsets = []
            for subset in subsets:
                newsubset = subset.copy()
                newsubsets.append(newsubset)
            for newsubset in newsubsets:
                newsubset.append(num)
            subsets.extend(newsubsets)
        
        return subsets
