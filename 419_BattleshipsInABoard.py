class Solution(object):
    def countBattleships(self, board):
        def search(x, y):
            board[x][y] = '.'
            if x + 1 < row:
                if board[x + 1][y] == 'X':
                    for i in range(x + 1, row):
                        if board[i][y] == 'X':
                            board[i][y] = '.'
                        else:
                            break
            if y + 1 < col:
                if board[x][y + 1] == 'X':
                    for j in range(y + 1, col):
                        if board[x][j] == 'X':
                            board[x][j] = '.'
                        else:
                            break


        row = len(board)
        col = len(board[0])

        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    count += 1
                    search(i, j)
        return count 
