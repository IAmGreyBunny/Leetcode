# Last updated: 10/12/2026, 4:46:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        def dfs(root,i):
            if root.left is None and root.right is None:
                if i == 1:
                    leaves1.append(root.val)
                else:
                    leaves2.append(root.val)
            else:
                if root.left != None:
                    dfs(root.left,i)
                if root.right != None:
                    dfs(root.right,i)

        dfs(root1,1)
        dfs(root2,2)

        print(leaves1)
        print(leaves2)

        if len(leaves1) == len(leaves2):
            for i in range(0,len(leaves1)):
                if leaves1[i] != leaves2[i]:
                    return False
            return True
        else:
            return False
        
        
                