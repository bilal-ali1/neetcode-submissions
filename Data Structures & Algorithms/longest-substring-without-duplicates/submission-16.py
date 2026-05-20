class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        l, r = 0, 1
        while len(s) > 1 and l < len(s) - 1:
            r = l + 1
            charSet = set([])
            currLen = 1
            charSet.add(s[l])
            while r < len(s) and s[r] not in charSet:
                currLen += 1
                charSet.add(s[r])
                res = max(currLen, res)
                r += 1
            l += 1
        return res