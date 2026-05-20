class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = []
        for i in range(len(position)):
            positionSpeed.append([position[i], speed[i]])
        positionSpeed = sorted(positionSpeed)

        stack = []

        for ps in positionSpeed[::-1]:
            reachingTime = (target - ps[0]) / ps[1]
            stack.append(reachingTime)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)