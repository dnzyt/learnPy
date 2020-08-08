class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self,
                             root: 'TreeNode',
                             p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, q, p)
        right = self.lowestCommonAncestor(root.right, p, q)
        return left if right is None else right if left is None else root
