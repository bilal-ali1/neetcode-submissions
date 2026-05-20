# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def dfs(root):
            if root == None:
                return [0, True]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[1] and right[1]) and (abs(left[0] - right[0]) < 2)
        
            return [1 + max(dfs(root.right)[0], dfs(root.left)[0]), balanced]

        return dfs(root)[1]
            
