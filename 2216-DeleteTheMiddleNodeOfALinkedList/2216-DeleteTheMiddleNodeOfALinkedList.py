# Last updated: 11/30/2025, 5:39:44 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        mid_start = head
        end = head
        
        while end.next is not None:
            # Move 1
            end = end.next
            prev = mid_start
            mid_start = mid_start.next
            # Move again
            if end.next is not None:
                end = end.next

        # Deletes node
        print("deleting: ")
        print(mid_start.val)
        
        if prev:
            if prev.next:
                prev.next = prev.next.next
            else:
                prev.next = None
        else:
            return None
            
        return head
        