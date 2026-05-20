class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pvisited = set()
        avisited = set()

        def dfs(row, col, visited, height):
            if row < 0 or col < 0 or row == rows or col == cols or (row, col) in visited or heights[row][col] < height:
                return
            if heights[row][col] >= height:
                visited.add((row, col))
                dfs(row + 1, col, visited, heights[row][col])
                dfs(row - 1, col, visited, heights[row][col])
                dfs(row, col + 1, visited, heights[row][col])
                dfs(row, col - 1, visited, heights[row][col])

        for col in range(cols):
            dfs(0, col, pvisited, heights[0][col])
            dfs(rows - 1, col, avisited, heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row, 0, pvisited, heights[row][0])
            dfs(row, cols - 1, avisited, heights[row][cols - 1])
        
        res = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pvisited and (row, col) in avisited:
                    res.append([row, col])

        return res

            


