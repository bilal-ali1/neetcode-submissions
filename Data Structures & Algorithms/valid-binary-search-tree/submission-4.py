# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkNode(root, lowerBound, upperBound):
            if root == None:
                return True
            if not (root.val > lowerBound and root.val < upperBound):
                return False
            
            return checkNode(root.right, root.val, upperBound) and checkNode(root.left, lowerBound, root.val)
        
        return checkNode(root, -1001, 1001)

