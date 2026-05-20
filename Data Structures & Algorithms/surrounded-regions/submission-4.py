class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Find all the Os on the edges

        # All 0s connected to those 0s are unable to be fully sorrounded

        # Identify all 0s unable to be changed, then go through and change
        # all other 0s

        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        notSorroundedSet = set()

        def dfs(row, col):
            if (row < 0 or row >= rows or col < 0 or col >= cols 
                or board[row][col] == "X" or board[row][col] == "T"):
                return
            
            board[row][col] = "T"
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        # Identifying the edge 0s:
        for row in range(rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][cols - 1] == "O":
                dfs(row, cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O":
                notSorroundedSet.add((0, col))
                dfs(0, col)
            if board[rows - 1][col] == "O":
                notSorroundedSet.add((rows - 1, col))
                dfs(rows - 1, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        