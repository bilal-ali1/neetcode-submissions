class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(s) - 1
        while (l < r):
            if not s[r] == s[l]:
                return False
            r -= 1
            l += 1
        return True