class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0] = nums[-1]
        dp[1] = nums[-2]

        for i in range(2, len(nums)):
            print(nums[-i - 1])
            dp[i] = nums[-i - 1] + max(dp[0 : i - 1])
        
        return max(dp)