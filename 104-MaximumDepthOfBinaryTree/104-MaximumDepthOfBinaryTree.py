# Last updated: 11/30/2025, 5:39:59 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            max_depth = 0
            left_depth = 0
            right_depth = 0 

            if root is None:
                return 0
            elif root.left is None and root.right is None:
                return 1+max_depth
            else:
                if root.left is not None:
                    left_depth = dfs(root.left)
                if root.right is not None:
                    right_depth = dfs(root.right)
            
            return 1+max(left_depth,right_depth)
        
        return dfs(root)
        