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
