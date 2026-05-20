# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If Both p and q are none: return True
        if not p and not q:
            return True

        # if one is none and the other isnt, return False
        if not p or not q:
            return False

        # If both are not none, check values
        if p.val != q.val:
            return False


        # do this for all subtrees/children
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)