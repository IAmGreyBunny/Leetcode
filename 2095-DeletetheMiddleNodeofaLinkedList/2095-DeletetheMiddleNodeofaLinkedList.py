# Last updated: 12/15/2025, 12:27:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9        # Edge Cases
10        if head == None or head.next == None:
11            return None
12
13        # Declarations
14        mid = head
15        end = None
16        if head.next.next != None:
17            end = head.next.next
18        else:
19            mid.next = None
20            return head
21
22        while True:
23            if end.next != None and end.next.next==None:
24                mid = mid.next
25                mid.next = mid.next.next
26                return head
27
28            if end.next != None and end.next.next != None:
29                end = end.next.next
30                mid = mid.next
31            else:
32                mid.next = mid.next.next
33                return head