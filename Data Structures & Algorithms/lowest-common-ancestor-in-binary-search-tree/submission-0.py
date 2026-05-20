# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def containsNode(root, node):
            if root == None:
                return False
            if root.val == node.val:
                return True
            return containsNode(root.right, node) or containsNode(root.left, node)

        returnStack = []
        toVisitStack = []
        if containsNode(root, p) and containsNode(root, q):
            returnStack.append(root)
        if root.right:
            toVisitStack.append(root.right)
        root = root.left
        while toVisitStack:
            if root == None:
                root = toVisitStack.pop()
            if containsNode(root, p) and containsNode(root, q):
                returnStack.append(root)
            if root.right:
                toVisitStack.append(root.right)
            root = root.left        
        
        return returnStack[-1]
            