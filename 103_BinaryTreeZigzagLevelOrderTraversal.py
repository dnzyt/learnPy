from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        res = []
        flip = 1

        while len(dq) != 0:
            temp = deque([])
            level = []
            for node in dq:
                level.append(node.val)
                if flip > 0:
                    if node.left:
                        temp.appendleft(node.left)
                    if node.right:
                        temp.appendleft(node.right)
                else:
                    if node.right:
                        temp.appendleft(node.right)
                    if node.left:
                        temp.appendleft(node.left)
            dq = temp
            flip = -1 * flip
            res.append(level)
        return res
