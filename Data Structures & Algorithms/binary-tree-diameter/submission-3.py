# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        
        def depth(node):
            nonlocal maxDiam
            if not node:
                return 0
            diam = 1 + max(depth(node.right), depth(node.left))
            maxDiam = max(maxDiam, depth(node.right) + depth(node.left))
            return diam

        depth(root)
        
        return maxDiam