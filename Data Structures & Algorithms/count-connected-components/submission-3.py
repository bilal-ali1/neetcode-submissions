class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        if edges == []:
            return n
        adj = {}
        for i in range(n):
            adj[i] = []
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return

        components = 1
        for i in range(n):
            origVisited = len(visited)
            dfs(i)
            if len(visited) == n:
                return components
            if len(visited) > origVisited:
                components += 1
        