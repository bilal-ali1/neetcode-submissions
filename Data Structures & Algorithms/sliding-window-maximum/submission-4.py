class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        l = 0
        r = k - 1
        ret = []
        for i in range(r + 1):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        ret.append(q[0])
        r += 1
        l += 1
        while r < len(nums):
            if q[0] == nums[l - 1]:
                q.popleft()
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            r += 1
            l += 1
            ret.append(q[0])
        return ret
