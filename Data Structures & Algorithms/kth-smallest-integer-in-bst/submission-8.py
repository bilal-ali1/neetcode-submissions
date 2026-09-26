# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # could add everything into a minheap adn then just keep poppin
        self.ret = []
        def preOrder(root):
            if not root:
                return
            preOrder(root.left)
            self.ret.append(root.val)
            preOrder(root.right)
        preOrder(root)
        smallest = root.val
        for i in range(k):
            smallest = self.ret[i]
        return smallest

