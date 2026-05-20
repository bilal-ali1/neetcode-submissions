class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1CharDict = {}
        s2CharDict = {}

        for char in s1:
            s1CharDict[char] = s1CharDict.get(char, 0) + 1
        
        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            s2CharDict[s2[i]] = s2CharDict.get(s2[i], 0) + 1

        while r < len(s2):
            if s2CharDict == s1CharDict:
                return True
            print(s2CharDict)
            s2CharDict[s2[l]] = s2CharDict.get(s2[l]) - 1
            if s2CharDict.get(s2[l]) == 0:
                del s2CharDict[s2[l]]
            l += 1
            if r < len(s2) - 1:
                r += 1
                s2CharDict[s2[r]] = s2CharDict.get(s2[r], 0) + 1
            else: 
                r += 1
        
        return False