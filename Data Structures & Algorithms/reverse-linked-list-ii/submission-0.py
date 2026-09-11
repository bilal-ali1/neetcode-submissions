# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        leftPrev = dummy
        for i in range(left - 1):
            leftPrev = leftPrev.next
            curr = curr.next
        
        # Reverse Group
        prev = None
        for j in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        newRight = leftPrev.next
        newRight.next = curr
        leftPrev.next = prev

        return dummy.next
        
        

        