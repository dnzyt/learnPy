class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        current = [root]
        res = []
        while current:
            next_level = []
            temp = []
            for node in current:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            res.append(temp)
        return res[::-1]
