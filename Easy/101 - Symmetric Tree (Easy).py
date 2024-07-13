# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, leftRoot: Optional[TreeNode], rightRoot: Optional[TreeNode]) -> bool:
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        
        return self.helper(leftRoot.left, rightRoot.right) and self.helper(leftRoot.right, rightRoot.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        return self.helper(root.left, root.right)