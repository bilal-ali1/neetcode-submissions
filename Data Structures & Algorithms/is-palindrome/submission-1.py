class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        r = len(s) - 1
        while not (l > r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True