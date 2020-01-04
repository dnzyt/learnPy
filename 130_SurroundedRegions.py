class Solution(object):
    def solve(self, board):
        def search(ix, jx):
            if ix < 0 or jx < 0 or ix >= row or jx >= col:
                return
            if board[ix][jx] == 'O':
                board[ix][jx] = 'Y'
                search(ix + 1, jx)
                search(ix - 1, jx)
                search(ix, jx + 1)
                search(ix, jx - 1)

        if not board:
            return
        row = len(board)
        col = len(board[0])
        for i in range(row):
            if board[i][0] == 'O':
                search(i, 0)
            if board[i][col - 1] == 'O':
                search(i, col - 1)
        for j in range(col):
            if board[0][j] == 'O':
                search(0, j)
            if board[row - 1][j] == 'O':
                search(row - 1, j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'













            
