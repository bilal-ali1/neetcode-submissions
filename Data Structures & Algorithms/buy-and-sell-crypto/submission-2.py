class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxProf = 0
        for i in range(len(prices)):
            if prices[i] <= prices[buy]:
                buy = i
                sell = i
            if prices[i] >= prices[sell]:
                sell = i
            prof = prices[sell] - prices[buy]
            maxProf = max(prof, maxProf)
        return maxProf

