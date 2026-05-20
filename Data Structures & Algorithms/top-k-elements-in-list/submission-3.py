class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        indexArray = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        for num, freq in freqDict.items():
            indexArray[freq].append(num)
        
        res = []
        for i in range(len(indexArray) - 1, 0, -1):
            for num in indexArray[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        