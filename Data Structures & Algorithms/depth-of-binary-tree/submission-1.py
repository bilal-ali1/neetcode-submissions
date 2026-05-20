# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        toVisit = [[root, 1]]
        while toVisit:
            currNode, depth = toVisit.pop()
            if not currNode == None:
                maxDepth = max(depth, maxDepth)
                toVisit.append([currNode.right, depth + 1])
                toVisit.append([currNode.left, depth + 1])
        return maxDepth