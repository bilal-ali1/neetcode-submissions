class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for char in s:
            sdict[char] = sdict.get(char, 0) + 1
        
        for char in t:
            tdict[char] = tdict.get(char, 0) + 1
        
        return tdict == sdict
       