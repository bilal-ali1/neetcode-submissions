# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        q = deque()
        q.append(root)
        while q:
            curLevel = []
            for i in range(len(q)):
                curNode = q.popleft()
                if curNode:
                    curLevel.append(curNode.val)
                    q.append(curNode.left)
                    q.append(curNode.right)
            if curLevel:
                levels.append(curLevel)
        
        return levels