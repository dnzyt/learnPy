from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seq = 0
        res = []
        while matrix:
            if seq == 0:
                res += matrix[0]
                matrix = matrix[1:]
            elif seq == 1:
                temp = []
                for row in matrix:
                    temp.append(row.pop())
                if not matrix[0]:
                    matrix = []
                res += temp
            elif seq == 2:
                res += reversed(matrix[-1])
                matrix = matrix[:-1]
            elif seq == 3:
                temp = []
                for row in reversed(matrix):
                    temp.append(row.pop(0))
                if not matrix[0]:
                    matrix = []
                res += temp
            seq = (seq + 1) % 4
        return res

    # recursive solution
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []
        col = len(matrix[0])

        res = matrix[0]
        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col - 1])
            for i in range(col - 2, -1, -1):
                res.append(matrix[row - 1][i])
            if col > 1:
                for i in range(row - 2, 0, -1):
                    res.append(matrix[i][0])
        m = []
        for i in range(1, row - 1):
            m.append(matrix[i][1:-1])

        return res + self.spiralOrder2(m)
