from tpying import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        indexOfRoot = inorder.index(root.val)
        root.left = self.buildTree(
            preorder[1:indexOfRoot+1], inorder[:indexOfRoot])
        root.right = self.buildTree(
            preorder[indexOfRoot+1:], inorder[indexOfRoot+1:])
        return root
