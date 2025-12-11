# Last updated: 12/11/2025, 6:28:33 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head == None:
9            return None
10        elif head.next == None:
11            return head
12
13        prev = None
14        current = head
15
16        while(current != None):
17            if current.next != None:
18                temp = current.next
19            else:
20                temp = None
21            
22            current.next = prev
23            prev = current
24            if temp != None:
25                current = temp
26            else:
27                return current
28
29
30
31
32            
33