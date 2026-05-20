class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # There should be no cycles
        if not n:
            return True
        nodeToNei = {}
        for i in range(n): # O(n)
            nodeToNei[i] = []
        # Populate: O(n)
        for node1, node2 in edges:
            nodeToNei[node1].append(node2)
            nodeToNei[node2].append(node1)
        visitingSet = set()
        
        def dfs(node, fromNode):
            # if node in visited set, all good 
            if node in visitingSet:
                return False
            visitingSet.add(node)
            # Not in visiting set, first time we are seeing it:
            for nei in nodeToNei[node]:
                if nei == fromNode or nei == -1:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        if len(visitingSet) != n:
            return False
        return True

            
