class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def getParent(node):
            p = parent[node]
            if p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def createUnions(node1, node2):
            p1 = getParent(node1)
            p2 = getParent(node2)

            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for node1, node2 in edges:
            if not createUnions(node1, node2):
                return [node1, node2]