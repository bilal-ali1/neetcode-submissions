class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Brute Force (Space): add everything to a set, then check if the number is in the set
        # Contains Duplicate, O(n) space

        # Brute Force (Time): Go through every node, checking the rest of the list until you
        # find the one that is duplicated (O(n^2)) time

        slow, fast = 0, 0

        while True:
            fast = nums[fast]
            fast = nums[fast]

            slow = nums[slow]

            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow2



        
        

