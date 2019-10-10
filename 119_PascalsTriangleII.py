class Solution:
    def getRow(self, rowIndex):
        res = [1] + [0] * rowIndex
        for i in range(rowIndex):
            for j in range(i + 1, 0, -1):
                res[j] = res[j] + res[j - 1]
        return res
