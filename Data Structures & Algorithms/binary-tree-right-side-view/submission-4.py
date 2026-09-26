# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Go layer by layer, add every node, then just return the last element in every layer?
        q = collections.deque([root])
        ret = []
        while q:
            rightSide = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(rightSide.left)
                    q.append(rightSide.right)
            if rightSide:
                ret.append(rightSide.val)
        
        return ret


                

            