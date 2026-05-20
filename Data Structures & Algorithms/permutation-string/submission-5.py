class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        sortedSub = sorted(s1)
        l, r = 0, len(s1) - 1

        while r < len(s2):
            if sorted(s2[l : r + 1]) == sortedSub:
                return True
            r += 1
            l += 1
        
        return False
