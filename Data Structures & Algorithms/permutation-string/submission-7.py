class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l, r = 0, len(s1) # O(klogk)
        while r <= len(s2):
            print(sorted(s2[l:r]))
            if sorted(s2[l: r]) == s1:
                return True
            l += 1
            r += 1
        
        return False