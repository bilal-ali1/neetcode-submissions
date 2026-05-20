class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        res = 0
        letterFreq = {}
        l, r = 0, 0
        while r < len(s):
            letterFreq[s[r]] = 1 + letterFreq.get(s[r], 0)
            if (r - l + 1) - max(letterFreq.values()) <= k:
                res = max(res, r - l + 1)
                r += 1
            else:
                letterFreq[s[l]] -= 1
                l += 1
                r += 1
        return res
