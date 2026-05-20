# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the Length (One Pass)
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        

        # Then go through again and remove the (Length - n)th node (Another Pass)
        dummy = ListNode()
        dummy.next = head
        current = dummy
        counter = 0
        while current.next and counter < (length - n):
            current = current.next
            counter += 1
        
        if current.next:
            current.next = current.next.next
        else:
            current.next = None

        return dummy.next

        

        # return



        

