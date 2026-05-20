class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict1 = {}
        dict2 = {}
    
        for char in s1: # O(m)
            dict1[char] = dict1.get(char, 0) + 1
        for char in s2[:len(s1)]:
            dict2[char] = dict2.get(char, 0) + 1
        
        l = 0

        for r in range(len(s1), len(s2)):
            if dict1 == dict2:
                return True
            dict2[s2[l]] -= 1
            if dict2[s2[l]] == 0:
                del dict2[s2[l]]
            l += 1
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1
        return dict1 == dict2

