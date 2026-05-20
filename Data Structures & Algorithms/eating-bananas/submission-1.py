class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Sort Piles
        maximum = max(piles)
        r = maximum
        l = 1
        minRate = r
        while (r >= l):
            rate = (r + l) // 2
            timeTaken = sum(math.ceil(pile / rate) for pile in piles)
            if timeTaken > h: # need a faster rate
                l = rate + 1
            elif timeTaken <= h:
                minRate = min(rate, minRate)
                r = rate - 1

        return minRate


        