"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        NodeToCopy = {None : None}
        while curr:
            copy = Node(curr.val)
            NodeToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            NodeToCopy[curr].next = NodeToCopy[curr.next]
            NodeToCopy[curr].random = NodeToCopy[curr.random]
            curr = curr.next
        
        return NodeToCopy[head]
