class Solution:
    def solveNQueens(self, n):
        res = []

        def dfs(queens, xydiff, xysum):
            row = len(queens)
            if n == row:
                res.append(queens)
                return None
            for col in range(n):
                if col not in queens and row - col not in xydiff and row + col not in xysum:
                    dfs(queens + [col], xydiff +
                        [row - col], xysum + [row + col])
        dfs([], [], [])
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in cols] for cols in res]
