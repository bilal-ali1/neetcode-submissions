class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        numFresh = 0
        minutes = 0

        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    numFresh += 1
        
        def bfs(row, col):
            nonlocal numFresh
            nonlocal q
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or grid[row][col] == 2:
                return
            if grid[row][col] == 1:
                grid[row][col] = 2
                q.append((row, col))
                numFresh -= 1
    

        while q:
            currFresh = numFresh
            for i in range(len(q)):
                row, col = q.popleft()
                bfs(row + 1, col)
                bfs(row - 1, col)
                bfs(row, col + 1)
                bfs(row, col - 1)
            if numFresh < currFresh:
                minutes += 1
        
        if numFresh == 0:
            return minutes
        return -1
