# Last updated: 12/11/2025, 6:29:12 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        current = head
10
11        while(current != None):
12            if current.next != None:
13                temp = current.next
14            else:
15                temp = None
16            
17            current.next = prev
18            prev = current
19
20            if temp != None:
21                current = temp
22            else:
23                return current
24        
25        return current
26
27
28
29
30            
31