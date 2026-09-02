class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 1, 1
        for i in range(1, n):
            two, one = one, one + two
        return one
