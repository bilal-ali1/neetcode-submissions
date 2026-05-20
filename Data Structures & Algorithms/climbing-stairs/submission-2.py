class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        OneStep = 1
        TwoStep = 2
        for i in range(2,n):
            temp = OneStep + TwoStep
            OneStep = TwoStep
            TwoStep = temp
        return TwoStep