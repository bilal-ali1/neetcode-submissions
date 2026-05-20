class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(s) - 1
        while not (left > right):
            if not (s[left] == s[right]):
                return False
            else:
                right -= 1
                left += 1
        return True