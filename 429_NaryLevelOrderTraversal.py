class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        nextLevel = [root]
        while nextLevel:
            temp = []
            curr = []
            for item in nextLevel:
                curr.append(item.val)
                temp += item.children
            res.append(curr)
            nextLevel = temp
        return res
