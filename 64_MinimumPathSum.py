class Solution:
    def minPathSum(self, grid):
        row = len(grid)
        col = len(grid[0])
        trans = [[0] * col for j in range(row)]
        trans[0][0] = grid[0][0]

        for i in range(1, row):
            trans[i][0] = trans[i - 1][0] + grid[i][0]
        for j in range(1, col):
            trans[0][j] = trans[0][j - 1] + grid[0][j]
        for i in range(1, row):
            for j in range(1, col):
                trans[i][j] = grid[i][j] + \
                    min(trans[i - 1][j], trans[i][j - 1])

        return trans[row - 1][col - 1]
