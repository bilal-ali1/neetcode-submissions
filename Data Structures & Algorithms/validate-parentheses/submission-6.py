class Solution:
    def isValid(self, s: str) -> bool:
        parenStack = []
        for char in s:
            if char == ')':
                if not parenStack or not parenStack.pop() == '(':
                    return False
            elif char == ']':
                if not parenStack or not parenStack.pop() == '[':
                    return False
            elif char == '}':
                if not parenStack or not parenStack.pop() == '{':
                    return False
            else:
                parenStack.append(char)
        
        if not parenStack:
            return True
        else:
            return False

            



        