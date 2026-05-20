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
        # First add all the nodes into a hashSet
        NodeDict = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            NodeDict[curr] = copy

            curr = curr.next
        
        
        # Now go through the list once more:

        curr2 = head
        while curr2:
            copy = NodeDict[curr2]
            copy.next = NodeDict[curr2.next]
            copy.random = NodeDict[curr2.random]

            curr2 = curr2.next
            
        
        return NodeDict[head]

