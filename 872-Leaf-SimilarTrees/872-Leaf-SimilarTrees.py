# Last updated: 12/10/2025, 11:44:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        leaves1 = []
10        leaves2 = []
11        def dfs(root,i):
12            if root.left is None and root.right is None:
13                if i == 1:
14                    leaves1.append(root.val)
15                else:
16                    leaves2.append(root.val)
17            else:
18                if root.left != None:
19                    dfs(root.left,i)
20                if root.right != None:
21                    dfs(root.right,i)
22
23        dfs(root1,1)
24        dfs(root2,2)
25
26        print(leaves1)
27        print(leaves2)
28
29        if len(leaves1) == len(leaves2):
30            for i in range(0,len(leaves1)):
31                if leaves1[i] != leaves2[i]:
32                    return False
33            return True
34        else:
35            return False
36        
37        
38                