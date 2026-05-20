class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = 0
        left = len(numbers) - 1
        while right < left:
            if (numbers[right] + numbers[left]) > target:
                left -= 1
            elif (numbers[right] + numbers[left]) < target:
                right += 1
            else:
                return [right + 1, left + 1]
 
        