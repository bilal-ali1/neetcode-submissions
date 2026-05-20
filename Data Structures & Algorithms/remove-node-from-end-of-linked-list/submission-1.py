# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of the list, N
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        
        # remove N - nth node
        len2 = 0
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        while len2 < (length - n):
            pointer = pointer.next
            len2 += 1
        
        pointer.next = pointer.next.next

        return dummy.next
        

       

