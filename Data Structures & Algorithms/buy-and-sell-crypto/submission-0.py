class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        sellPrice = prices[0]
        for price in prices:
            if price > buyPrice:
                sellPrice = price
                profit = sellPrice - buyPrice
                maxProfit = max(maxProfit, profit)
            if price < buyPrice:
                buyPrice = price
                sellPrice = price
        
        return maxProfit



        