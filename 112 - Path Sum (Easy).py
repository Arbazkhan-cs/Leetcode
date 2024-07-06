# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode], targetSum: int, actualSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return actualSum+root.val == targetSum

        return self.helper(root.left, targetSum, actualSum + root.val) or self.helper(root.right, targetSum, actualSum + root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, targetSum, 0)
        