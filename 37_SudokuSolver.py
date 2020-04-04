from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        if not board:
            return
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(0, 9):
            if board[row][i] != '.' and board[row][i] == c:
                return False
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' \
                    and \
                    board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] \
                    == c:
                return False
        return True

    def solveSudoku2(self, board):
        rows = [set(range(1, 10)) for _ in range(9)]
        cols = [set(range(1, 10)) for _ in range(9)]
        blocks = [set(range(1, 10)) for _ in range(9)]
        empty = []

        def helper(count=0):
            if count == len(empty):
                return True
            i, j = empty[count]
            b = 3 * (i // 3) + (j // 3)
            for num in rows[i] & cols[j] & blocks[b]:
                board[i][j] = str(num)
                rows[i].remove(num)
                cols[j].remove(num)
                blocks[b].remove(num)
                if helper(count + 1):
                    return True
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    blocks[b].add(num)
            return False

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    blocks[3 * (i // 3) + j // 3].remove(val)
        helper()
