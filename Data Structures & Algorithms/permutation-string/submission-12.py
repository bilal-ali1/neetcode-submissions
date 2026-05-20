class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Dict = {}
        for char in s1:
            s1Dict[char] = 1 + s1Dict.get(char, 0)
        
        s2Dict = {}
        l , r = 0, len(s1) - 1
        for i in range(l , r + 1):
            s2Dict[s2[i]] = 1 + s2Dict.get(s2[i], 0) 
        
        while r < len(s2):
            print(s2Dict)
            print(s1Dict)
            if s2Dict == s1Dict:
                return True

            s2Dict[s2[l]] -= 1
            if s2Dict[s2[l]] == 0:
                del(s2Dict[s2[l]])

            l += 1

            r += 1
            if r < len(s2):
                s2Dict[s2[r]] = 1 + s2Dict.get(s2[r], 0)
            
        return False
            
