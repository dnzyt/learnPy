class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(i, j, idx):
            if i < 0 or j < 0 or i >= row or j >= col or idx >= len(word):
                return False
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            curr = board[i][j]
            board[i][j] = '0'
            res = search(i - 1, j, idx + 1) or search(i + 1, j, idx + 1) or search(i, j - 1, idx + 1) or search(i, j + 1, idx + 1)
            board[i][j] = curr
            return res

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if search(i, j, 0):
                    return True
        return False
