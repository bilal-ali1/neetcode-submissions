class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return
            else:
                grid[row][col] = '0'
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    numIslands += 1
                    dfs(row, col)
        
        return numIslands
                