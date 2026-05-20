"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToCopy = {None : None}
        def nodeSearch(node):
            if node in nodeToCopy:
                return nodeToCopy[node]
            nodeToCopy[node] = Node(node.val)
            for neighbor in node.neighbors:
                nodeToCopy[node].neighbors.append(nodeSearch(neighbor))
            return nodeToCopy[node]
        
        return nodeSearch(node)