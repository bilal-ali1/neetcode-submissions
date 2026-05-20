class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        stack.append([0, temperatures[0]])
        retList = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                retList[stack[-1][0]] = index - stack[-1][0]
                stack.pop()
            stack.append([index, temp])

        return retList
