class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: None
        """
        if not root:
            return root
        q = [root]
        while q:
            sz = len(q)
            for i in range(sz):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i == sz - 1:
                    continue
                curr.next = q[0]
        return root


