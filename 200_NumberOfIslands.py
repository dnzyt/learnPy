class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                else:
                    count += 1
                    self.sink(grid, i, j)
        return count

    def sink(self, grid, x, y):
        if grid[x][y] == '0':
            return 0
        grid[x][y] = '0'
        if x - 1 >= 0 and grid[x - 1][y] == '1':
            self.sink(grid, x - 1, y)
        if x + 1 < len(grid) and grid[x + 1][y] == '1':
            self.sink(grid, x + 1, y)
        if y - 1 >= 0 and grid[x][y - 1] == '1':
            self.sink(grid, x, y - 1)
        if y + 1 < len(grid[0]) and grid[x][y + 1] == '1':
            self.sink(grid, x, y + 1)
        return 1

    def numIslands2(self, grid):
        m = len(grid)
        n = len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        count = m * n
        p = [i for i in range(m * n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for k in range(4):
                        if i + dx[k] >= 0 \
                                and i + dx[k] < m \
                                and j + dy[k] >= 0 \
                                and j + dy[k] < n:
                            if grid[i + dx[k]][j + dy[k]] == "1":
                                p1 = self._parent(
                                    p, (i + dx[k]) * n + (j + dy[k]))
                                p2 = self._parent(p, i * n + j)
                                if p1 != p2:
                                    self._union(
                                        p,
                                        (i + dx[k]) * n + (j + dy[k]),
                                        (i * n) + j
                                    )
                                    count -= 1
                else:
                    count -= 1

        return count

    def _parent(self, p, i):
        root = i
        while root != p[root]:
            root = p[root]
        return root

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        if p1 != p2:
            p[p2] = p1
        return
