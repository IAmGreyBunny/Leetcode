# Last updated: 12/18/2025, 8:58:33 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        # Edge Case
10        if head == None or head.next == None:
11            return head
12
13        current_odd = head
14        current_even = even_head = head.next
15
16        while current_even and current_even.next != None:
17            current_odd.next = current_even.next
18            current_odd = current_odd.next
19            current_even.next = current_odd.next
20            current_even = current_even.next
21
22        current_odd.next = even_head
23        return head