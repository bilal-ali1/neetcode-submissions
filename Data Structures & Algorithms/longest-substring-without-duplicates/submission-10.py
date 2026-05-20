class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l = 0
        while (l < len(s) - 1):
            r = l + 1
            length = 1
            characterSet = set()
            characterSet.add(s[l])
            while (r < len(s)) and s[r] not in characterSet:
                characterSet.add(s[r])
                length += 1
                r += 1
            maxlen = max(maxlen, length)
            l += 1
        if len(s) == 1:
            return 1
        return maxlen

