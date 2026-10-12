# Last updated: 10/12/2026, 4:45:44 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge Cases
        if head == None or head.next == None:
            return None

        # Declarations
        mid = head
        end = None
        if head.next.next != None:
            end = head.next.next
        else:
            mid.next = None
            return head

        while True:
            if end.next != None and end.next.next==None:
                mid = mid.next
                mid.next = mid.next.next
                return head

            if end.next != None and end.next.next != None:
                end = end.next.next
                mid = mid.next
            else:
                mid.next = mid.next.next
                return head