class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search the rows, using a similar method that we did for the binary search

        # Then, once appropriate row is found, we can apply binary search on the row

        # this will yield Log(m * n) solutions

        # Row search:
        r = len(matrix) - 1
        l = 0
        while (r >= l):
            m = (r + l) // 2
            if (target > matrix[m][-1]):
                l = m + 1
            elif (target < matrix[m][0]):
                r = m - 1

            # Col Search
            else:
                break
        if not (r >= l):
            return False
        else:
            m = (r + l) // 2
            rcol, lcol = len(matrix[m]) - 1, 0
            while (rcol >= lcol):
                mcol = (rcol + lcol) // 2
                if (target > matrix[m][mcol]):
                    lcol = mcol + 1
                elif (target < matrix[m][mcol]):
                    rcol = mcol - 1
                else:
                    return True
            return False
        