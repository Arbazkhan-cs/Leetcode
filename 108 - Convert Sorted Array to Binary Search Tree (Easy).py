# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, start: int, end: int, nums: List[int]) -> Optional[TreeNode]:
        if start > end:
            return None
        mid = start + (end-start) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(start, mid-1, nums)
        root.right = self.helper(mid+1, end, nums)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(0, len(nums)-1, nums)