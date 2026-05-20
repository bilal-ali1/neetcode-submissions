class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        for token in tokens:
            if token == '+':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num1 + num2)
            
            elif token == '-':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num2 - num1)

            elif token == '*':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(num1 * num2)
            
            elif token == '/':
                num1 = numStack.pop()
                num2 = numStack.pop()
                numStack.append(int(float(num2) / num1))
            else:
                numStack.append(int(token))
        if numStack:
            return numStack[-1]
