# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = {root.val}
        stack = [root.left, root.right]
        while stack:
            curr = stack.pop()
            if curr:
                if k - curr.val in s:
                    return True
                else:
                    s.add(curr.val)
                    stack.extend([curr.left, curr.right])
        return False




