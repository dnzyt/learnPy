class Solution:
    def findCircleNum(self, M):
        le = len(M)
        p = [i for i in range(le)]
        count = le

        def _parent(i):
            root = p[i]
            while root != p[root]:
                root = p[root]
            while i != p[i]:
                x = p[i]
                p[i] = root
                i = x
            return root

        def _union(i, j):
            rootI = _parent(i)
            rootJ = _parent(j)
            if rootI == rootJ:
                return
            p[rootI] = rootJ
            nonlocal count
            count -= 1

        for i in range(le):
            for j in range(i, le):
                if M[i][j] == 1:
                    _union(i, j)
        return count
