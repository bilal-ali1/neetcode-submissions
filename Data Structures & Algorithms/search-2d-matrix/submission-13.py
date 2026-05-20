class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = len(matrix) - 1
        top = 0

        # Check which row, log(m):
        while bottom >= top:
            current_row = (top + bottom) // 2
            if matrix[current_row][-1] < target:
                top = current_row + 1
            elif matrix[current_row][0] > target:
                bottom = current_row - 1
            else:
                print("found Row!")
                right = len(matrix[current_row]) - 1
                left = 0
                while right >= left:
                    curr = (right + left) // 2
                    if matrix[current_row][curr] > target:
                        right = curr - 1
                    elif matrix[current_row][curr] < target:
                        left = curr + 1
                    else:
                        return True
                return False
        return False
