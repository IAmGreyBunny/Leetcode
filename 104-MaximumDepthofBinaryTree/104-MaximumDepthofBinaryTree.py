# Last updated: 12/9/2025, 9:12:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if root == None:
10            return 0
11
12        def dfs(tree):
13            if tree.left == None and tree.right == None:
14                return 1
15            else:
16                depth_left = depth_right = 1
17                if tree.left != None:
18                    print("left tree exist")
19                    depth_left+=dfs(tree.left)
20                if tree.right != None:
21                    print("right tree exist")
22                    depth_right+=dfs(tree.right)
23                return max(depth_left,depth_right)
24        
25        return dfs(root)