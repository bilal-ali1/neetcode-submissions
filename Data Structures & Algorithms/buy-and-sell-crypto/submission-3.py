class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxProf = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            prof = prices[sell] - prices[buy]
            maxProf = max(maxProf, prof)
            sell += 1
        return maxProf
        

