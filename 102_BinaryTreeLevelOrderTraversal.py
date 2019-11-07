class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            node = []
            l = []
            for i in queue:
                l.append(i.val)
                if i.left:
                    node.append(i.left)
                if i.right:
                    node.append(i.right)
            res.append(l)
            queue = node
        return res
