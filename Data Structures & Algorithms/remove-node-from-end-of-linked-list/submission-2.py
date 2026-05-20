# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        dummy = ListNode()
        dummy.next = head
        ptr = dummy
        counter = 0
        while ptr.next and counter < (length - n):
            ptr = ptr.next
            counter+= 1

        ptr.next = ptr.next.next

        return dummy.next