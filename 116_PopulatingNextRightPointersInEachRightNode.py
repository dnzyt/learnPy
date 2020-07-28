from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        ns = deque([])

        def bfs(root):
            dq = deque([root])
            while len(dq) != 0:
                curr = dq.popleft()
                ns.append(curr)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
        level = 0
        bfs(root)
        while len(ns) != 0:
            numOfElems = 2 ** level
            for i in range(numOfElems):
                curr = ns.popleft()
                if i == numOfElems - 1:
                    break
                curr.next = ns[0]
            level += 1
        return root

    def connect2(self, root: Node) -> Node:
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect2(root.left)
            self.connect2(root.right)
        return root
