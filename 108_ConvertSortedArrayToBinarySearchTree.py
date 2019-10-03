class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        return self.to_bst(0, len(nums) - 1, nums)

    def to_bst(self, start, end, nums):
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = TreeNode(nums[mid])
        node.left = self.to_bst(start, mid - 1, nums)
        node.right = self.to_bst(mid + 1, end, nums)
        return node
