class Solution:
    def shortestPathBinaryMatrix(self, grid):
        q = [(0, 0, 2)]
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        elif n <= 2:
            return n

        for i, j, d in q:
            for x, y in [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j + 1),
                (i + 1, j + 1),
                (i + 1, j),
                (i + 1, j - 1),
                (i, j - 1)
            ]:
                if x == n - 1 and y == n - 1:
                    return d
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    q.append((x, y, d + 1))
                    grid[x][y] = 1
        return -1
