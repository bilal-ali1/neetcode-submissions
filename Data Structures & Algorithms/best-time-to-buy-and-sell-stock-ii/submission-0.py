class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                totalProfit += (prices[r] - prices[l])
            l = r
            r += 1
        return totalProfit

                
            
            