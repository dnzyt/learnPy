class Solution:
    def generate(self, numRows):
        res = []
        for i in range(0, numRows):
            res.append([])
            for j in range(0, i + 1):
                if j in (0, i):
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
        return res
