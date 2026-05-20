class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        l, r = 0, 1
        charSet = set([])
        charSet.add(s[l])
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            currLen = r - l + 1
            res = max(res, currLen)
            r += 1
        return res