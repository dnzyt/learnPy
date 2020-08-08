class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pointer = root
        while pointer:
            if p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left
            elif p.val > pointer.val and q.val > pointer.val:
                pointer = pointer.right
            else:
                return pointer

    # 没有用的BST性质，对普通二叉树的操作
    def lowestCommonAncestor2(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        return left if right is None else right if left is None else root

    # 利用BST的特点， 如果p, q分别在两边，那么当前root就是LCA
    def lowestCommonAncestor3(self, root, p, q):
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor3(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor3(root.right, p, q)
        return root
