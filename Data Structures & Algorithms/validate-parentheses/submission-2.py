class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to solve it
        # if the parenthesi
        closeToOpen = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for i in range(len(s)):
            if (s[i] in closeToOpen):
                if stack and (closeToOpen[s[i]] == stack[-1]):
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(s[i])
        if not stack:
            return True
        else:
            return False


            



        