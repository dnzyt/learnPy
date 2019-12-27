class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        self.inorderTraversal(root, output)
        res = float('inf')
        for i in range(1, len(output)):
            res = min(res, output[i] - output[i - 1])
        return res


    def inorderTraversal(self, root, output):
        if root is None:
            return
        self.inorderTraversal(root.left, output)
        output.append(root.val)
        self.inorderTraversal(root.right, output)
