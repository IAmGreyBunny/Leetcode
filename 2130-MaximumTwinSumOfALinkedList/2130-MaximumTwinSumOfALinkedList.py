# Last updated: 10/12/2026, 4:45:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    from collections import deque

    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head:
            return None

        stack = deque()

        # first traversal
        cur = head
        
        while(cur):
            stack.append(cur.val)
            cur = cur.next

        # second traversal
        cur = head
        max_val = 0

        while(cur):
            cur_sum = cur.val + stack.pop()
            max_val = cur_sum if cur_sum > max_val else max_val
            cur = cur.next

        return max_val