# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if root == None:
                return 0
            
            if root.val >= maxVal:
                res = 1
                maxVal = root.val
            else:
                res = 0
            res += dfs(root.right, maxVal)
            res += dfs(root.left, maxVal)
            return res
        return dfs(root, root.val)