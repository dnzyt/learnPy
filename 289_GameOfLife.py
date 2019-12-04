class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0]) if row > 0 else 0

        for i in range(row):
            for j in range(col):
                lives = 0
                for x in range(max(0, i - 1), min(row - 1, i + 1) + 1):
                    for y in range(max(0, j - 1), min(col - 1, j + 1) + 1):
                        lives += (board[x][y] & 1)
                if lives == 3 or lives - board[i][j] == 3:
                    board[i][j] |= 0b10
        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
