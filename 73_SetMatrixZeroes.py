from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        leftedge, topedge = False, False
        
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    leftedge = True if j == 0 else leftedge
                    topedge = True if i == 0 else topedge
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if leftedge:
            for i in range(0, m):
                matrix[i][0] = 0
        if topedge:
            for j in range(0, n):
                matrix[0][j] = 0