class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacificVisited = set()
        atlanticVisited = set()

        # DFS function to check:
        def dfs(row, col, prevHeight, vset):
            if (row < 0 or row >= rows or col < 0 or col >= cols
                or heights[row][col] < prevHeight or (row, col) in vset):
                return
            vset.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, heights[row][col], vset)

        # Track which cells are bordered to atlantic and pacific
        for row in range(rows):
            dfs(row, 0, heights[row][0], pacificVisited)
            dfs(row, len(heights[0]) - 1, heights[row][len(heights[0]) - 1], atlanticVisited)

        
        for col in range(cols):
            dfs(0, col, heights[0][col], pacificVisited)
            dfs(len(heights) - 1, col, heights[len(heights) - 1][col], atlanticVisited)
        

        res = []
        for row, col in pacificVisited:
            if (row, col) in atlanticVisited:
                res.append([row, col])
        return res