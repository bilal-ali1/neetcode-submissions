# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Employ merge two sorted lists
        if not lists:
           return None
        
        res = ListNode(0)
        curr = res
        
        def mergeLists(list1, list2):
            res = ListNode()
            curr = res
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            return res.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if (i + 1) < len(lists):
                    merged.append(mergeLists(lists[i], lists[i + 1]))
                else:
                    merged.append(mergeLists(lists[i], None))
            lists = merged

        
        return lists[0]

        
        
        


            


