# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ret = 0
        def dfs(root, prevMax):
            if not root:
                return
            if prevMax <= root.val:
                prevMax = root.val
                self.ret += 1
            dfs(root.right, prevMax)
            dfs(root.left, prevMax)
        dfs(root, -101)
        return self.ret    