class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        return self.get_height(root) >= 0

    def get_height(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
