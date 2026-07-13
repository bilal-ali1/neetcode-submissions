class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        if not len(s) == len(t):
            return False
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1
        return (sDict == tDict)