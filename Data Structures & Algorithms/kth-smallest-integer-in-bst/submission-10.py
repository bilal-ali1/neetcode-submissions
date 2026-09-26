# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ret = []
        def preOrder(root):
            if not root or len(self.ret) == k:
                return
            preOrder(root.left)
            if len(self.ret) == k:
                return
            else:
                self.ret.append(root.val)
            preOrder(root.right)
        preOrder(root)
        return self.ret[-1]

