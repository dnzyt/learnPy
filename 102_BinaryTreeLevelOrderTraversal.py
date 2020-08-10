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
            ls = []
            for i in queue:
                ls.append(i.val)
                if i.left:
                    node.append(i.left)
                if i.right:
                    node.append(i.right)
            res.append(ls)
            queue = node
        return res

    # DFS
    def levelOrder2(self, root):
        res = []

        def helper(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 0)

        return res
