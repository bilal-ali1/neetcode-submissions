class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visit = set()
        def dfs(row, col):
            nonlocal perimeter
            nonlocal directions
            if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in visit:
                if grid[row][col] == 1:
                    visit.add((row, col))
                    cellPerim = 0
                    for dr, dc in directions:
                        if 0 <= row + dr < rows and 0 <= col + dc < cols and grid[row + dr][col + dc] == 1:
                            dfs(row + dr, col + dc)
                        else:
                            cellPerim += 1
                    perimeter += cellPerim

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
        return perimeter