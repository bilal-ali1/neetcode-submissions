# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if leaf, then max path is self.val
        # otherwise its the max of node, node + right, node + left, and node + left and right
        # propogate up for nodes.

        # base cases:

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            leftMax = max(leftMax, 0)
            rightMax = dfs(root.right)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + rightMax + leftMax)
            return root.val + max(rightMax, leftMax)
        dfs(root)
        return max(res)
