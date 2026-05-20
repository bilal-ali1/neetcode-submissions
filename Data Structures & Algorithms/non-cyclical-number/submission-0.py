class Solution:
    def isHappy(self, n: int) -> bool:
        seenSet = set()
        while not (n in seenSet):
            if n == 1:
                return True
            seenSet.add(n)
            digits = [int(digit) for digit in str(n)]
            n = 0
            for digit in digits:
                n += (digit * digit)
        return False
            



        