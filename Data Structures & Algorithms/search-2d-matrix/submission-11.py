class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        foundRow = -1
        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                foundRow = middle
                break
        if foundRow < 0:
            return False
        else:
            l, r, = 0, len(matrix[foundRow]) - 1
            while (l <= r):
                mid = (r + l) // 2
                if matrix[middle][mid] > target:
                    r = mid - 1
                elif matrix[middle][mid] < target:
                    l = mid + 1
                else:
                    return True
            return False