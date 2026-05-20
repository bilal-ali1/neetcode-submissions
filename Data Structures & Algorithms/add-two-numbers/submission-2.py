# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while carry or l1 or l2:
            if not l1:
                num1 = 0
            else:
                num1 = l1.val
                l1 = l1.next
            if not l2:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next
            curr.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10
            curr = curr.next
        
        return dummy.next
            


            