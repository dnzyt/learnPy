from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        diaglen = size // 2
        for i in range(diaglen):
            for j in range(i, size - 1 - i):
                matrix[i][j], \
                    matrix[j][size - i - 1], \
                    matrix[size - i - 1][size - 1 - j], \
                    matrix[size - 1 - j][i] \
                    = \
                    matrix[size - 1 - j][i], \
                    matrix[i][j], \
                    matrix[j][size - i - 1], \
                    matrix[size - i - 1][size - 1 - j]
