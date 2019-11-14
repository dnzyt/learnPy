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
