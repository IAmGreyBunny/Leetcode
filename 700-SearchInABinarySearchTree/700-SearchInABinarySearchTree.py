# Last updated: 10/12/2026, 4:46:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def binarySearch(node,val):
            if node.val == val:
                return node
            elif val < node.val and node.left != None:
                return binarySearch(node.left,val)
            elif val > node.val and node.right != None:
                return binarySearch(node.right,val)
            else:
                return None

        return binarySearch(root,val)


        