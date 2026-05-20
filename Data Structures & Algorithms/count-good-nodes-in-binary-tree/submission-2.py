# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        goodNodes = 0

        def findGoodNodes(maxNode, root):
            nonlocal goodNodes
            if root == None:
                return 
            if root.val >= maxNode:
                goodNodes += 1
                findGoodNodes(root.val, root.right)
                findGoodNodes(root.val, root.left)
            else:
                findGoodNodes(maxNode, root.right)
                findGoodNodes(maxNode, root.left)
        
        findGoodNodes(root.val, root)

        return goodNodes
             