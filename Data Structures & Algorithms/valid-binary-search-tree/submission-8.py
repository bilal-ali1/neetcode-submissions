# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upperBound = 1001
        lowerBound = -1001
        def isValid(root, upperBound, lowerBound):
            if root == None:
                return True
            if root.val >= upperBound or root.val <= lowerBound:
                return False
            else:
                return isValid(root.left, root.val, lowerBound) and isValid(root.right, upperBound, root.val)
        
        return isValid(root, upperBound, lowerBound)  