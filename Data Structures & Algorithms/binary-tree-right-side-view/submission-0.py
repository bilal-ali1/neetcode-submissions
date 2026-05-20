# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BST, only return the last element in each row
        returnList1 = []
        returnList2 = []
        q = collections.deque()
        q.append(root)
        while q:
            list = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if list:
                returnList1.append(list)
        for list in returnList1:
            returnList2.append(list[-1])
        return returnList2


