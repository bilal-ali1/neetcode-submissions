class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        minutes = 0
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    numFresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
        
        def bfs(row, col):
            nonlocal numFresh
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0 or grid[row][col] == 2:
                return
            if grid[row][col] == 1:
                grid[row][col] = 2
                q.append((row, col))
                numFresh -= 1

        while q:
            currentFresh = numFresh
            for i in range(len(q)):
                rottenRow, rottenCol = q.popleft()
        
                bfs(rottenRow + 1, rottenCol)
                bfs(rottenRow - 1, rottenCol)
                bfs(rottenRow, rottenCol + 1)
                bfs(rottenRow, rottenCol - 1)
            if currentFresh > numFresh:
                minutes += 1
        
        if numFresh == 0:
            return minutes
        return -1
        
