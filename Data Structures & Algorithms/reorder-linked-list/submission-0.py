# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the second half of the list
        # reverse the second half of the list
        # join the nodes newly reversed 2nd half 
        # with original order first half in alternating order
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
        
        
    
        

            