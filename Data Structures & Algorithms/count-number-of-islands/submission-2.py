class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        numIslands = 0

        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == '0':
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numIslands += 1
                    dfs(row, col)
        
        return numIslands
        
        
                