class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        minRate = right

        while right >= left:
            current_rate = (right + left) // 2
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / current_rate)
            if hours_taken > h:
                left = current_rate + 1
            else:
                minRate = min(current_rate, minRate)
                right = current_rate - 1
        
        return minRate

        