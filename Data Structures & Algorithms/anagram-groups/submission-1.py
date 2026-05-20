class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}
        returnlist = []
        for word in strs:
            anagram = "".join(sorted(word))
            if anagram not in anaDict:
                anaDict[anagram] = [word]
            else:
                anaDict[anagram].append(word)
            
        return anaDict.values()

        



