# Last updated: 12/11/2025, 12:21:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        def binarySearch(node,val):
10            if node.val == val:
11                return node
12            elif val < node.val and node.left != None:
13                return binarySearch(node.left,val)
14            elif val > node.val and node.right != None:
15                return binarySearch(node.right,val)
16            else:
17                return None
18
19        return binarySearch(root,val)
20
21
22        