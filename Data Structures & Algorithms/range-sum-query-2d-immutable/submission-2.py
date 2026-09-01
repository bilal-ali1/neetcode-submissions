class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.prefixSum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]

                self.prefixSum[row + 1][col + 1] = prefix + self.prefixSum[row][col + 1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        above = self.prefixSum[row1][col2 + 1]
        left = self.prefixSum[row2 + 1][col1]
        topLeft = self.prefixSum[row1][col1]
        return self.prefixSum[row2 + 1][col2 + 1] - above - left + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)