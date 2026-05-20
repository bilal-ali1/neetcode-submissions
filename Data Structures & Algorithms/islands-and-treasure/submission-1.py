class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col, dist):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] < dist:
                return
            if grid[row][col] > 0:
                grid[row][col] = dist
            
            bfs(row + 1, col, dist + 1)
            bfs(row - 1, col, dist + 1)
            bfs(row, col + 1, dist + 1)
            bfs(row, col - 1, dist + 1)
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    bfs(row, col, 0)
        
        
