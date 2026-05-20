# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        ptr = head
        counter = 0
        while not ptr.next == None:
            if ptr.next.val > -1 and ptr.next.val <= counter:
                return True
            ptr = ptr.next
            counter += 1
        return False
            
         