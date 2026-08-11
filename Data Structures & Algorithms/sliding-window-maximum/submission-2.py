class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        #k: length of the sublist
        r = k - 1
        l = 0
        q = deque()
        q.append(nums[0])
        ret = []
        # initial add
        for i in range(1, r + 1):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        ret.append(q[0])
        r += 1
        l += 1
        while r < len(nums):
            if q[0] == nums[l - 1]:
                q.popleft()
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            ret.append(q[0])
            r += 1
            l += 1
        return ret

            


