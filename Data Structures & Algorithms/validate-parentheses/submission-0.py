class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                # check if the most recently opened corresponds
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # pop removes the most recent
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False
