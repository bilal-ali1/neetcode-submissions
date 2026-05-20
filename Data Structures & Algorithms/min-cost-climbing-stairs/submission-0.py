class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0, 0)
        cost.insert(len(cost), 0)
        print(cost)
        dp = [0] * (len(cost) + 1)
        dp[1] = cost[-1]
        dp[2] = cost[-2]
        print(dp)
        for i in range(3, len(cost) + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[-i]
        print(dp)
        
        return dp[-1]
