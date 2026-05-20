class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        returnArr = []
        for i in range(len(temperatures)):
            found = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    found = 1
                    returnArr.append(j - i)
                    break
            if found == 0:
                returnArr.append(0)
        return returnArr

                