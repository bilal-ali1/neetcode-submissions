class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])

        posSpeed = sorted(posSpeed)

        print(posSpeed)

        stack = []

        for pos, speed in posSpeed[::-1]:
            reachingTime = (target - pos) / speed
            if not stack or reachingTime > stack[-1]:
                stack.append(reachingTime)
            

        print(stack)
        return len(stack)