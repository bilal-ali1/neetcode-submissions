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
        boolList = []
        def dfs(root):
            if root == None:
                return 0
            return 1 + max(dfs(root.right), dfs(root.left))
        
        toVisitStack = [TreeNode()]
        while toVisitStack:
            if abs(dfs(root.right) - dfs(root.left)) > 1:
                return False
            else:
                boolList.append(True)
            
            if root.right:
                toVisitStack.append(root.right)
            if root.left:
                root = root.left
            else:
                root = toVisitStack.pop()
        
        return True
            