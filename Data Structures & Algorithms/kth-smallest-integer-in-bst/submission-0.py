# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque()
        q.append(root)
        nodeList = []
        
        while q:
            list = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if list:
                for node in list:
                    nodeList.append(node)
        heapq.heapify(nodeList)
        print(nodeList)
        for i in range(k - 1):
            print(heapq.heappop(nodeList))
        print(nodeList)
        return nodeList[0]

            
