# Last updated: 12/25/2025, 4:10:05 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7
8    from collections import deque
9
10    def pairSum(self, head: Optional[ListNode]) -> int:
11        
12        if not head:
13            return None
14
15        stack = deque()
16
17        # first traversal
18        cur = head
19        
20        while(cur):
21            stack.append(cur.val)
22            cur = cur.next
23
24        # second traversal
25        cur = head
26        max_val = 0
27
28        while(cur):
29            cur_sum = cur.val + stack.pop()
30            max_val = cur_sum if cur_sum > max_val else max_val
31            cur = cur.next
32
33        return max_val